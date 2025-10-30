from mail import Mail
from flask import Flask, render_template, request
import requests


posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET'])
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact", methods=['POST'])
def receive_data():
    msg = "Successfully sent the messages"
    user_data = {
        "name": request.form['name'],
        'message': request.form['message'],
        'phone_number': request.form['phone'],
        'email': request.form['email'],
    }
    print(user_data)
    mail = Mail(user_data['name'], user_data['message'], user_data['phone_number'], user_data['email'])
    mail.load_email()
    return render_template("contact.html", data = msg)
if __name__ == "__main__":
    app.run(debug=True, port=5001)
