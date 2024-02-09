#!/usr/bin/env python3
'''defines code for internationalisationof a flask  app'''
from flask_babel import Babel
from typing import Dict, Union
from flask import render_template, Flask, request, g


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
    '''selecte teh best matching language for a given locale
    it uses priority to determine which one to choose
    Return
    string repreenting the locale
    '''
    #  priorty 1 locale in url
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    # priority 2 if locale in settings
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']

    # if locale in the header
    locale = request.headers.get('locale')
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    # default locale
    return request.accept_languages.best_match(Config.LANGUAGES)


users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
        }


def get_user() -> Union[Dict, None]:
    '''get a user if the id is passed or if the login_as request parameter
    is passed

    Return:
    A user dict or None'''
    user_id = request.args.get('login_as')
    if user_id:
        user_id = int(user_id)
    return users.get(user_id)


@app.before_request
def before_request() -> None:
    '''get a user and set the user as a global variable'''
    login_user = get_user()
    g.user = login_user


@app.route('/')
def index() -> str:
    '''create a flask route to render a template'''

    return render_template('5-index.html', login_user=g.user)


if __name__ == '__main__':
    app.run()
