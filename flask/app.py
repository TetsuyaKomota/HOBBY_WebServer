#-*- coding:utf-8 -*-

from subprocess import check_output
from flask import Flask, redirect, request, render_template
from utils.decorator_auth import requires_auth

from setting import HOSTNAME, PORT

app = Flask(__name__)

@app.before_request
#@requires_auth
def basic_auth():
    pass

@app.route("/")
def index():
    return render_template("index.html")
    # return agent.talk("hogehoge")


if __name__ == "__main__":
    app.run( debug = True, host=HOSTNAME, port=PORT)
