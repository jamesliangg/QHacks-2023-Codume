from flask import Flask, request, render_template
from main import *
from latexFormat import *

app = Flask(__name__)
sampleData = ['']

@app.route("/")
def homePage():
    writeExperiences()
    return render_template("index.html")

# @app.route("/", methods = ['GET','POST'])
# def homePage():
#     if request.method == "POST":
#         print("hello world")
#         #print (request.form.get("str"))
#         # sampleData.append(request.form.get("str"))
#         f = request.files['the_file']
#         #print(the_data)
#     writeFile()
#     print("hello world2")
#     return render_template("index.html")

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         # f.save('/var/www/uploads/uploaded_file.txt')
#         print("hello world2")
