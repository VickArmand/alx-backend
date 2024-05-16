#!/usr/bin/env python3
"""Babel setup"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)
app.url_map.strict_slashes = False

users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
        }


class Config:
    """configuration class"""
    LANGUAGES = ["en", "fr"]

    def __init__(self) -> None:
        """initialize by changing default language to en and timezone to utc"""
        app.config['BABEL_DEFAULT_LOCALE'] = self.LANGUAGES[0]
        app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
        app.config.from_object(Config())


@app.route('/')
def home() -> str:
    """
    Create a single / route and an index.html template
    that simply outputs “Welcome to Holberton” as page title (<title>)
    and “Hello world” as header (<h1>).
    """
    status = 'You are not logged in.'
    if g.user:
        status = f'You are logged in as {g.user.name}.'
    return render_template('6-index.html', status)


@babel.localeselector
def get_locale():
    """Get locale from request"""
    query = request.query_string.decode('utf-8').split('locale=')
    if len(query) == 2:
        locale = query[1]
        if locale in app.config['LANGUAGES']:
            return locale
    user = getattr(g, 'user', None)
    if user is not None and user.locale in app.config['LANGUAGES']:
        return user.locale
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    returns a user dictionary or None
    if the ID cannot be found or if login_as was not passed.
    """
    query = request.query_string.decode('utf-8').split('login_as=')
    if len(query) == 2:
        id = int(query[1])
        if id in users.keys():
            return users[id]
    return None


@app.before_request
def before_request():
    """
    executed before all other functions.
    before_request should use get_user to find a user if any,
    and set it as a global on flask.g.user
    """
    user = get_user()
    if user:
        g.user = user


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
