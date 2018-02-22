from flask import render_template
from app import app
from FindSystemInformation.main import main
import os
os.system("export FLASK_APP=/Users/gavin/Desktop/Semester2/comp30670/FlaskApp/views.py")
@app.route('/')
def index():
        returnDict = {}
        returnDict['title'] = 'Home'
        returnDict['sysInfo'] = main()
        return render_template("index.html", **returnDict) 
