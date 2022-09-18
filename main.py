from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/e7d10eebdead68a7fb09").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/blog")
def about():
    return render_template("blog.html")


@app.route("/log_in_page")
def contact():
    return render_template("log_in_page.html")

if __name__ == "__main__":
    app.run(debug=True)
