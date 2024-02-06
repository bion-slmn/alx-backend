#!/usr/bin/env python3
'''create a basic flask app'''
from flask_babel import Babel
from flask import render_template, Flask


app = Flask(__name__)
babel = Babel(app)


class Config:
    '''configuring the languages supported by app'''
    LANGUAGES = ["en", "fr"]


Config.BABEL_DEFAULT_LOCALE = 'en'
Config.BABEL_DEFAULT_TIMEZONE = 'UTC'
app.config.from_object(Config)


@app.route('/')
def index() -> str:
    '''create a flask route to render a template'''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
