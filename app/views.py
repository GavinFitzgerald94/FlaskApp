from flask import render_template
from app import app
from FindSystemInformation.main import main
import os
os.system("/Users/gavin/Desktop/Semester2/comp30670/FlaskApp/app")
@app.route('/')
def index():
        returnDict = {}
        returnDict['title'] = 'Home'
        returnDict['sysInfo'] = main()
        return render_template("index.html", **returnDict) 
