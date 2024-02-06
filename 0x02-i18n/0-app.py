#!/usr/bin/env python3
'''create a basic flask app'''
from flask import render_template, Flask


app = Flask(__name__)


@app.route('/')
def index():
    '''create a flask route to render a template'''
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run()
