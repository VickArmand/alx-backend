#!/usr/bin/env python3
"""Babel setup"""
from flask_babel import Babel, refresh
from flask import Flask, render_template
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
        refresh()


@app.route('/')
def home() -> str:
    """
    Create a single / route and an index.html template
    that simply outputs “Welcome to Holberton” as page title (<title>)
    and “Hello world” as header (<h1>).
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
