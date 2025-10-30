from os import unsetenv

from flask import Flask

app = Flask(__name__)
def make_bold(function):
    def bolder_text():
        return f'<b>{function()}</b>'

    return bolder_text

def make_emphasis(function):
    def emphasis_text():
        return f"<em>{function()}</em>"

    return emphasis_text

def make_underlined(function):
    def underline_text():
        return f"<u>{function()}</u>"

    return underline_text

@app.route("/")
def hello_world():
    return "<p style='text-align: center'>Hello, World!</p>"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "<p>Bye </p>"

@app.route("/username/<name>")
def greet(name):
    return f"<p>Hello {name}!!"

if __name__ == "__main__":
    app.run(debug=True)