from flask import Flask, request, render_template
from main import *

app = Flask(__name__)
sampleData = 'sample data'

@app.route("/")
def homePage():
    return render_template("index.html", data = sampleData)