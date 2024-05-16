#!/usr/bin/env python3
"""Babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)
app.url_map.strict_slashes = False


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
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """Get locale from request"""
    query = request.query_string.decode('utf-8').split('locale=')
    if len(query) == 2:
        locale = query[1]
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
