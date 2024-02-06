#!/usr/bin/env python3
''' Infer appropriate time zone
'''
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    '''configure defaults'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


babel.timezoneselector
def get_timezone() -> str:
    '''get time zone'''
    loc_zone = request.args.get('timezone')
    if not loc_zone and g.user is not None:
        loc_zone = g.user.get('timezone')
    if loc_zone:
        try:
            pytz.timezone(loc_zone)
            return loc_zone
        except pytz.UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']
    return app.config['BABEL_DEFAULT_TIMEZONE']


@babel.localeselector
def get_locale():
    '''get local language'''
    loc_lang = request.args.get('locale')
    if loc_lang in app.config['LANGUAGES']:
        return loc_lang
    elif g.user is not None:
        loc_lang = g.user.get('locale')
        if loc_lang in app.config['LANGUAGES']:
            return loc_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    '''login user'''
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    '''befor request fun'''
    g.user = get_user()


@app.route('/')
def home():
    '''route(/)'''
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(debug=True)
