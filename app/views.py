from flask import render_template
from app import app
from FindSystemInformation.main import main
set FLASK_APP = views.py
flask run
@app.route('/')
def index():
        returnDict = {}
        returnDict['title'] = 'Home'
        returnDict['sysInfo'] = main()
        return render_template("index.html", **returnDict) 
