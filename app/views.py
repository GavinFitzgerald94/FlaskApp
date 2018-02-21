from flask import render_template
from app import app
from FindSystemInformation.main import main
@app.route('/')
def index():
        returnDict = {}
        returnDict['title'] = 'Home'
        returnDict['sysInfo'] = main()
        return render_template("index.html", **returnDict)
        
