from sys import path
path.append('..\\packages') # TBD check this..

##############

import json

from flask import Flask, request
from markdown import markdown
from pprint import pprint # for debug purposes..

from cnf import BASE_TITLE, DEBUG_MODE, LOGGER

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

@app.route('/readme')
def readme():
    file = open('README.md', 'r')
    html = markdown(file.read())
    return render('html.html', None, {'html': html})

@app.route('/changelog')
def changelog():
    file = open('log.md', 'r')
    html = markdown(file.read())
    return render('html.html', BASE_TITLE + " | Changelog", {'html': html})

@app.route('/documentation')
def documentation():
    file = open('doc.md', 'r')
    html = markdown(file.read())
    return render('html.html', BASE_TITLE + " | Documentation", {'html': html})

@app.route('/report')
def report():
    return render('index.html', BASE_TITLE + " | Report") # TBD implement this

@app.errorhandler(404)
def error_handler_404(error):
    return render('layout/empty.html', BASE_TITLE + " | Error", error), 404

@app.route('/test',
    methods = ['GET', 'POST']
)
def test():
    LOGGER.log_ok("Message Nr. " + str(request.json['payload']))
    return json.dumps(LOGGER.get_log())


if __name__ == '__main__':
    pprint(vars(app))
    app.run(debug = DEBUG_MODE)
