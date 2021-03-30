from flask import Flask, render_template

app = Flask(__name__, template_folder='templates') 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products/")
def shop():
    return render_template("Products.html")

@app.route("/about/")
def about():
    return render_template("About.html")

@app.route("/contact/")
def contact():
    return render_template("Contacts.html")