from flask import Flask, render_template
from data import Data
app = Flask(__name__)

@app.route('/')
def home():
    data = Data()
    return render_template("index.html", data=data.data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<post_id>")
def post(post_id):
    data = Data()
    data_post = []

    for items in data.data:
        if items['id'] == int(post_id):
            data_post.append(items)
    print(data_post)
    return render_template("post.html", post=data_post)

if __name__ == '__main__':
    app.run(debug=True)