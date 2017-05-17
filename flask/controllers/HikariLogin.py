#-*-coding: utf-8 -*-

import json
from flask import Flask, redirect, request, render_template, make_response
import time
from datetime import datetime

from setting import HIKARI_SESSION_TIME

def hikariLogin(request, hikariMain):

    # HIKARI の login を叩く
    status = hikariMain.login(request.form["user_name"], request.form["password"])

    # ログイン失敗ならその旨を JSON で返して終了
    output = {}
    output['result'] = status[0]
    output["message"] = status[1]
    if status[0] == False:
        return json.dumps(output, indent=4, ensure_ascii=False)
    else:
        # Cookie を作成する
        content = json.dumps(output, indent=4, ensure_ascii=False)
        response = make_response(content) 
        max_age = HIKARI_SESSION_TIME
        expires = int(time.mktime(datetime.now().timetuple())) + max_age
        response.set_cookie('login', value=status[1], max_age=max_age, expires=expires, path='/')
        return response
