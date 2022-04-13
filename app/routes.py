from flask import render_template

from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "James"}
    posts = [
        {
            "author": {"username": "John"},
            "body": "Beautiful day in Singapore!"
        },
        {
            "author": {"username": "Susan"},
            "body": "The Avengers movie was not so cool!"
        },
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)
