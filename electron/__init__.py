# main web app for all tasks

from flask import Flask, render_template
import json
import strings
import os

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    """" entry point for webapp """
    @app.route("/")
    def main():
        return render_template('index.html', topics=strings.library, my=strings.personal_data)

    return app