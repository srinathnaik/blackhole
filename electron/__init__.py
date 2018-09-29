# main web app for all tasks

from flask import Flask, render_template
import json
import strings
import os

# create and configure the app
app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('config.py', silent=True)


# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'

"""" entry point for webapp """
@app.route("/")
def main():
    return render_template('index.html', topics=strings.library, my=strings.personal_data)


if __name__ == '__main__':
    app.run()