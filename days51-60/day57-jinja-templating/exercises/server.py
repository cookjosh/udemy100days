from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    today_date = datetime.datetime.now()
    year = today_date.year
    return render_template("index.html", current_year = year)

@app.route("/guess/<user_name>")
def guess(user_name):
    agify_url = f"https://api.agify.io?name={user_name}"
    genderize_url = f"https://api.genderize.io?name={user_name}"
    user_age = ((requests.get(url=agify_url)).json())["age"]
    user_gender = ((requests.get(url=genderize_url)).json())["gender"]
    return render_template("guess.html", name=user_name.capitalize(), age=user_age, gender=user_gender)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)