#!/usr/bin/env python3
'''   Parametrize templates
'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    '''configure defaults'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)




def get_locale():
    '''get local language'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Babel(app, locale_selector=get_locale)

@app.route('/', strict_slashes=False)
def home():
    '''route(/)'''
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
