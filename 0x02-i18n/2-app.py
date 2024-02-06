#!/usr/bin/env python3
'''   Get locale from request
'''
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''configure defaults'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    return request.accept_languages(app.config['LANGUAGES'])


@app.route('/')
def home():
    '''route(/)'''
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
