#-*- coding:utf-8 -*-

from subprocess import check_output
from flask import Flask, redirect, request, render_template, make_response
from utils.decorator_auth import requires_auth
import json

import time
from datetime import datetime

from setting import HOSTNAME, PORT
# TODO この辺汚いからうまい書き方を考える
from models.hikari import HikariMain

from controllers.BookInsert import bookInsert
from controllers.BookInfo import bookInfo
from controllers.HikariUserValidation import hikariUserValidation
from controllers.HikariCreateUser import hikariCreateUser
from controllers.HikariLogin import hikariLogin
from controllers.HikariStartConversation import hikariStartConversation
from controllers.HikariTalk import hikariTalk
from controllers.HikariEndConversation import hikariEndConversation

app = Flask(__name__)
hikari = HikariMain.Hikari()

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

@app.route("/login_room")
@requires_auth
def login_room():
    return render_template("loginRoom.html")

@app.route("/talk_room")
def talk_room():    
    # login が成功してるか，Cookie を取得して確認する
    status = request.cookies.get('login', None)
    if status is None:
        return redirect("/login_room")
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
# ------------------------------------------------------
    # ログイン処理用 API
        # ユーザー名のバリデーションチェック
@app.route("/api/hikari_user_validation", methods=["POST"])
def Api_HikariUserValidation():
    return hikariUserValidation(request.form, hikari)
        # 新規登録
@app.route("/api/hikari_create_user", methods=["POST"])
def Api_HikariCreateUser():
    return hikariCreateUser(request.form, hikari)
        #ログイン 
@app.route("/api/hikari_login", methods=["POST"])
def Api_HikariLogin():
    return hikariLogin(request.form, hikari)
# ------------------------------------------------------
    # メイン画面用 API
        # エージェント生成
@app.route("/api/hikari_start_conversation", methods=["GET"])
def Api_HikariStartConversation():
    return hikariStartConversation(request.args, hikari)
        # 対話を取得
@app.route("/api/hikari_talk", methods=["GET"])
def Api_HikariTalk():
    return hikariTalk(request.args, hikari)
        # エージェント削除
@app.route("/api/hikari_end_conversation", methods=["GET"])
def Api_HikariEndConversation():
    return hikariEndConversation(request.args, hikari)
 


if __name__ == "__main__":
    app.run( debug = True, host=HOSTNAME, port=PORT)
