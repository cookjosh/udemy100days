# Day 36 project - Stock Price and News text alert
# Steps and APIs provided from course
import datetime as dt
import html
import os
import requests
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Twilio vars
#proxy_client = TwilioHttpClient()
#proxy_client.session.proxies = {'https': os.environ['https_proxy']}
twilio_sid = os.environ["TWILIO_SID"]
twilio_token = os.environ["TWILIO_API_TOKEN"]

client = Client(twilio_sid, twilio_token,) #http_client=proxy_client)

## STEP 1: Use https://www.alphavantage.co
# Work out percent change between yesterday's close price and the day before's close price
stock_url = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": os.environ["STOCK_API_TOKEN"],
}

stock_response = requests.get(url=stock_url, params=stock_parameters)
stock_response.raise_for_status()
stock_data = (stock_response.json())["Time Series (Daily)"]

close_list = []
for key in stock_data.keys():
    daily_close = float(stock_data[key]["4. close"])
    close_list.append(daily_close)
yesterday_close_price = float(close_list[0])
before_yesterday_close_price = float(close_list[1])
price_change = float(yesterday_close_price - before_yesterday_close_price)
percent_change = float("%.2f" % (price_change * 100 / before_yesterday_close_price))

if percent_change < 0:
    stock_change = "🔻"
elif percent_change > 0:
    stock_change = "🔺"

before_yesterday_shift = float(("%.2f" % (before_yesterday_close_price * .05)))


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_url = "https://newsapi.org/v2/everything"
news_date = str(dt.datetime.now().date())
news_parameters = {
    "q": COMPANY_NAME,
    "from": news_date,
    "sortBy": "popularity",
    "apiKey": os.environ["NEWS_API_TOKEN"]
}

# Create list of top 3 news articles to pull from
news_response = requests.get(url=news_url, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()["articles"]
news_headlines = []
for index in range(0, 3):
    article_dict = {
        "headline": html.unescape(news_data[index]["title"]),
        "brief": html.unescape(news_data[index]["description"]),
        "url": html.unescape(news_data[index]["url"]),
    }
    news_headlines.append(article_dict)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
text_message = f"""\n{STOCK} {stock_change}{percent_change}%\nHeadline: {news_headlines[0]['headline']}\nBrief: {news_headlines[0]['brief']}\n
Headline: {news_headlines[1]['headline']}\nBrief: {news_headlines[1]['brief']}\n
Headline: {news_headlines[2]['headline']}\nBrief: {news_headlines[2]['brief']}
"""

message = client.messages \
                .create(
                     body=text_message,
                     from_=os.environ["TWILIO_PHONE_NUMBER"],
                     to=os.environ["RECIPIENT_PHONE_NUMBER"]
                 )

print(message.sid)