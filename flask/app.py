#-*- coding:utf-8 -*-

from subprocess import check_output
from flask import Flask, redirect, request, render_template
from utils.decorator_auth import requires_auth
import json
import datetime

from setting import HOSTNAME, PORT
# TODO この辺汚いからうまい書き方を考える
from hikari import HikariMain
from controllers import RakutenBookInfo
from DBController import Inserter

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
    bookInfo = RakutenBookInfo.Api_getBookInfo(request.args.get("isbn", ""), datetime.date.today().isoformat())
    output['bodydata'] = bookInfo["bodydata"]
    output['isbn'] = bookInfo["isbn"]
    output['title'] = bookInfo["title"]
    output['author'] = bookInfo["author"]
    return json.dumps(output, indent=4, ensure_ascii=False)

@app.route("/api/book_insert", methods=["GET"])
def Api_BookInsert():
    token = Inserter.Inserter()
    token.changeConnection(dbName="PMAN_DB")
    values = {}
    if isinstance(request.args.get("isbn", ''), str):
        values["isbn"] = request.args.get("isbn", '').decode("utf-8")
    elif isinstance(request.args.get("isbn", ''), unicode):
        values["isbn"] = request.args.get("isbn", '')
 
    if isinstance(request.args.get("title", ''), str):
        values["title"] = request.args.get("title", '').decode("utf-8")
    elif isinstance(request.args.get("title", ''), unicode):
        values["title"] = request.args.get("title", '')

    if isinstance(request.args.get("author", ''), str):
        values["author"] = request.args.get("author", '').decode("utf-8")
    elif isinstance(request.args.get("author", ''), unicode):
        values["author"] = request.args.get("author", '')
 


    token.insert(tableName="booklist", values=values)
    output = {}
    output['success'] = True
    return json.dumps(output, indent=4, ensure_ascii=False)




if __name__ == "__main__":
    app.run( debug = True, host=HOSTNAME, port=PORT)
