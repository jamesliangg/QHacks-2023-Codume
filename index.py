from flask import Flask, request, render_template, Response
from main import *
from latexFormat import *

app = Flask(__name__)
sampleData = ['']
texData = ''

@app.route("/", methods = ['GET','POST'])
def homePage():
    return render_template("index.html")

@app.route("/getPlotCSV")
def getPlotCSV():
    experienceArray = writeExperiences()
    texData = writeResume('Canada',' ',' ',' ',experienceArray['name'],experienceArray['Summary'],experienceArray['Experience #1'][5],experienceArray['Experience #1'][4],'',' ',experienceArray['Experience #1'][0],' ',' ','','',' ',experienceArray['Experience #2'][0],' ',' ',experienceArray['Edcuation'],'','','','','','',experienceArray['email'],experienceArray['Phone'],experienceArray['Programming Languages'],'','','')
    # print(texData)
    return Response(
        texData,
        mimetype="text/tex",
        headers={"Content-disposition":
                 "attachment; filename=resume.tex"})

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
