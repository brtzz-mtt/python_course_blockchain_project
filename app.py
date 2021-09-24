from sys import path
path.append('..\\packages') # TBD check this..

##############

from flask import Flask, request # TBD check request
from markdown import markdown
from pprint import pprint # for debug purposes..

from cnf import BASE_TITLE, DEBUG_MODE

from app_functions import render

app = Flask(__name__)

@app.route('/')
def index():
    return render()

@app.route('/license')
def license():
    file = open('gpl.md', 'r')
    html = markdown(file.read())
    return render('html.html', BASE_TITLE + " | License", {'html': html})

@app.route('/changelog')
def changelog():
    file = open('README.md', 'r')
    html = markdown(file.read())
    return render('html.html', BASE_TITLE + " | Changelog", {'html': html})

@app.errorhandler(404)
def error_handler_404(error):
    return render('layout/empty.html', BASE_TITLE + " | Error", error), 404

if __name__ == '__main__':
    app.run(debug = DEBUG_MODE)
