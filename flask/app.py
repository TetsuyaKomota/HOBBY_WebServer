#-*- coding:utf-8 -*-

from subprocess import check_output
from flask import Flask, redirect, request, render_template
from utils.decorator_auth import requires_auth
import json
import datetime

from setting import HOSTNAME, PORT
# TODO この辺汚いからうまい書き方を考える
import HikariMain
from Controller import RakutenBookInfo

app = Flask(__name__)

Agents = {}

log = {}

@app.before_request
@requires_auth
def basic_auth():
    pass

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/admin")
@requires_auth
def admin():
    return render_template("admin.html")

@app.route("/talk_room")
def talk_room():
    Agents[len(Agents)] = HikariMain.Hikari()
    return render_template("talkRoom.html")

@app.route("/react_study")
@requires_auth
def react_study():
    return render_template("reactStudy.html")

@app.route("/book_info", methods=["GET"])
def book_info():
    return render_template("bookinfo.html")

@app.route("/now_making")
def now_making():
    return render_template("nowMaking.html")

# -------------------------------------------------
# API

@app.route("/api/book_info", methods=["GET"])
def Api_BookInfo():
    output = {}
    output['success'] = True
    output['bodydata'] = RakutenBookInfo.Api_getBookInfo(request.args.get("isbn", ""), datetime.date.today().isoformat())
    return json.dumps(output, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    app.run( debug = True, host=HOSTNAME, port=PORT)
