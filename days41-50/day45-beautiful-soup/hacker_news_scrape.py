# Exercise from day45
# Scraping a live website - Hacker News

from os import link
import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com")
yc_homepage = response.text

soup = BeautifulSoup(yc_homepage, "html.parser")
links = soup.find_all(name="a", class_="titlelink")

link_texts = []
link_urls = []

for link in links:
    link_text = link.getText()
    link_texts.append(link_text)
    link_url = link.get("href")
    link_urls.append(link_url)

link_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_score = max(link_upvotes)
max_index = link_upvotes.index(max_score)
print(link_texts)
print(link_urls)
print(link_upvotes)

highest_link = [link_texts[max_index], link_urls[max_index], link_upvotes[max_index]]
print(highest_link)