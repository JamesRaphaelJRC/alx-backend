#!/usr/bin/env python3
''' Basic Babel setup '''
from flask_babel import Babel
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


def get_locale() -> str:
    ''' Get user's locale '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


class Config(object):
    ''' Babel configuration. '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def helloWorld() -> str:
    '''
        Renders a template for Babel usage.
    '''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
