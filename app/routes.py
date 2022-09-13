from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/about")
def about():
    me = {
        "first_name" : "Megan",
        "last_name" : "Paquin",
        "hobbies" : "Crafts",
        "bio" : "enter bio here"
    }

    return render_template("about.html")