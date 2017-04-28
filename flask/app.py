#-*- coding:utf-8 -*-

from subprocess import check_output
from flask import Flask, redirect, request, render_template
from utils.decorator_auth import requires_auth
import json

from setting import HOSTNAME, PORT
# TODO この辺汚いからうまい書き方を考える
from models.hikari import HikariMain

from controllers.BookInsert import bookInsert
from controllers.BookInfo import bookInfo
from controllers.HikariStartConversation import hikariStartConversation
from controllers.HikariTalk import hikariTalk
from controllers.HikariChangeState import hikariChangeState
from controllers.HikariEndConversation import hikariEndConversation

app = Flask(__name__)


@app.before_request
def basic_auth():
    pass

@app.route("/")
@requires_auth
def index():
    return render_template("index.html")

@app.route("/admin")
@requires_auth
def admin():
    return render_template("admin.html")

@app.route("/talk_room")
def talk_room():
    
    return render_template("talkRoom.html")

@app.route("/react_study")
@requires_auth
def react_study():
    return render_template("reactStudy.html")

@app.route("/book_info", methods=["GET"])
@requires_auth
def book_info():
    return render_template("bookinfo.html")

@app.route("/now_making")
def now_making():
    return render_template("nowMaking.html")

# =============================================================================
# API

# -----------------------------------------------------------
# 蔵書DB 用 API
@app.route("/api/book_info", methods=["GET"])
def Api_BookInfo():
    return bookInfo(request.args)

@app.route("/api/book_insert", methods=["GET"])
def Api_BookInsert():
    return bookInsert(request.args)

# -----------------------------------------------------------
# ひかりちゃん用 API
    # エージェント生成
@app.route("/api/hikari_start_conversation", methods=["GET"])
def Api_HikariStartConversation():
    return hikariStartConversation(request.args, HikariMain)
    # 対話を取得
@app.route("/api/hikari_talk", methods=["GET"])
def Api_HikariTalk():
    return hikariTalk(request.args, HikariMain)
    # 感情遷移を取得
@app.route("/api/hikari_change_state", methods=["GET"])
def Api_HikariChangeState():
    return hikariChangeState(request.args, HikariMain)
    # エージェント削除
@app.route("/api/hikari_end_conversation", methods=["GET"])
def Api_HikariEndConversation():
    return hikariEndConversation(request.args, HikariMain)
 


if __name__ == "__main__":
    app.run( debug = True, host=HOSTNAME, port=PORT)
