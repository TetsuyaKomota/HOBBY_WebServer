#-*- coding:utf-8 -*-

from subprocess import check_output
from flask import Flask, redirect, request, render_template
from utils.decorator_auth import requires_auth
import json

from setting import HOSTNAME, PORT
# TODO この辺汚いからうまい書き方を考える
from lib.hikari import HikariMain

from controllers.BookInsert import bookInsert
from controllers.BookInfo import bookInfo


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
    return bookInfo(request.args)

@app.route("/api/book_insert", methods=["GET"])
def Api_BookInsert():
    return bookInsert(request.args)



if __name__ == "__main__":
    app.run( debug = True, host=HOSTNAME, port=PORT)
