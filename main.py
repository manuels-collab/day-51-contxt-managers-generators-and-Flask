from flask import Flask, render_template
from post import Post

app = Flask(__name__)

post = Post()
@app.route('/')
def home():
    global post
    return render_template("index.html", blog_post=post.blog_posts)

@app.route("/post/<blog_id>")
def get_blog_content(blog_id):
    global post
    blog_post = post.get_specified_blog(int(blog_id))
    print(blog_post)
    return render_template("post.html", post=blog_post)



if __name__ == "__main__":
    app.run(debug=True)
