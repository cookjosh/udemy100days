

from flask import Flask

app = Flask(__name__)

# Practice creating decorators to be used on routes
def make_bold(function):
    def bold_wrapper():
        return f"<b>{function()}</b>"
    return bold_wrapper

def make_italics(function):
    def italics_wrapper():
        return f"<em>{function()}</em>"
    return italics_wrapper

def make_underlined(function):
    def underline_wrapper():
        return f"<u>{function()}</u>"
    return underline_wrapper


@app.route("/")
def hello_world():
    return "<h1 style-'text-align: center'>Hello, World!</h1>" \
        "<p>This is a paragraph.</p>" \
        "<img src='https://media.giphy.com/media/yfhy4ll0dGth6QjNkf/giphy.gif' width=200>"

@app.route("/bye")
@make_bold
@make_underlined
@make_italics
def bye():
    return "Bye, Felicia."

@app.route("/<username>")
def show_username(username):
    return f"Hello, {username}!"


if __name__ == "__main__":
    app.run(debug=True)