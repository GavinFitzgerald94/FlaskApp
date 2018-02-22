from flask import render_template
from app import app
from FindSystemInformation.main import main
import os
os.system("set FLASK_APP=app.py")
@app.route('/')
def index():
        returnDict = {}
        returnDict['title'] = 'Home'
        returnDict['sysInfo'] = main()
        return render_template("index.html", **returnDict) 
