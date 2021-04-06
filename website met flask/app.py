from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return ("Welcome to my Flask web page! If you want to see more type behind localhost or 127.0.0.1:5000   /products  /about  or  /contact")

@app.route("/products/")
def shop():
    return render_template("Products.html")

@app.route("/about/")
def about():
    return render_template("About.html")

@app.route("/contact/")
def contact():
    return render_template("Contacts.html")