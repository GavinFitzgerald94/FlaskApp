from flask import render_template
from flask import FLASK_APP
from app import app
from FindSystemInformation.main import main
FLASK_APP=views.py
@app.route('/')
def index():
        returnDict = {}
        returnDict['title'] = 'Home'
        returnDict['sysInfo'] = main()
        return render_template("index.html", **returnDict) 
