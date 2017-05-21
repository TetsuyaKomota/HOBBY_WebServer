#-*-coding: utf-8 -*-

import json

from models.hikari import HikariMain
from models.hikari.HikariStatics import getStateKeyId

from lib.DBController import Ksql

k = Ksql.Ksql()

def hikariTalk(request, hikariMain):

    user_id = request.cookies.get('login', None)
    # login が成功してるか，Cookie を取得して確認する
    if user_id is None:
        output = {}
        output['success'] = False
        output['message'] = "cannot confirm login"
        return json.dumps(output, indent=4, ensure_ascii=False)
        
        
    talk_id = request.args.get("talk_id", '')
    query = request.args.get("query", '')
    
    # 返答と感情状態の取得
    reply = hikariMain.getReply(talk_id, query) 

    # talk_log に登録
    hikariMain.talk_log[talk_id].append({"state":reply["state"], "query":query, "response":reply["response"]})

    # DB に保存
    valuesdict = {}
    valuesdict[u"user_id"] = user_id
    valuesdict[u"talk_id"] = talk_id
    valuesdict[u"query"]   = query 
    valuesdict[u"state_key_id"] = getStateKeyId(reply["state"])
    valuesdict[u"response"]     = reply["response"]
    k.insert(u"talk_log", values = valuesdict)

    output = {}
    output['success'] = True
    output['state'] = reply["state"]
    output['response'] = reply["response"].encode("utf-8")

    return json.dumps(output, indent=4, ensure_ascii=False)
