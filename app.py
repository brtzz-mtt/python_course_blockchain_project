from sys import path
path.append('..\\packages') # TBD check this..

##############

from flask import Flask, render_template

from cnf import BASE_TITLE

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
    title = BASE_TITLE
)

if __name__ == '__main__':
    app.run(debug = True)
