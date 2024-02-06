#!/usr/bin/env python3
'''create a basic flask app'''
from flask_babel import Babel
from flask_babel import _
from flask import render_template, Flask, request


app = Flask(__name__)
babel = Babel(app)


class Config:
    '''configuring the languages supported by app'''
    LANGUAGES = ["en", "fr"]


Config.BABEL_DEFAULT_LOCALE = 'en'
Config.BABEL_DEFAULT_TIMEZONE = 'UTC'
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    '''selecte teh best matching language for a given locale'''
    locale = request.args.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index() -> str:
    '''create a flask route to render a template'''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
