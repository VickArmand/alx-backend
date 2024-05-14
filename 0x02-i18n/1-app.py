from flask_babel import Babel, refresh
from flask import Flask, render_template
app = Flask(__name__)
babel = Babel(app)


class Config:
    """configuration class"""
    LANGUAGES = ["en", "fr"]

    def __init__(self) -> None:
        """initialize by changing default language to en and timezone to utc"""
        app.config['BABEL_DEFAULT_LOCALE'] = self.LANGUAGES[0]
        app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route('/')
def home() -> None:
    """
    Create a single / route and an index.html template
    that simply outputs “Welcome to Holberton” as page title (<title>)
    and “Hello world” as header (<h1>).
    """
    app.config.from_object(Config())
    refresh()
    return render_template('1-index.html',
                           language=app.config['BABEL_DEFAULT_LOCALE'],
                           timezone=app.config['BABEL_DEFAULT_TIMEZONE'])
