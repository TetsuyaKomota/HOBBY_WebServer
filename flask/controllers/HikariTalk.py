#-*-coding: utf-8 -*-

import json
from models.hikari import HikariMain

def hikariTalk(args, hikariMain):

    talk_id = args.get("talk_id", '')
    query = args.get("query", '')
    
    # 返答と感情状態の取得
    reply = hikariMain.getReply(talk_id, query) 

    # talk_log に登録
    hikariMain.talk_log[talk_id].append({"state":reply["state"], "query":query, "response":reply["response"]})

    output = {}
    output['success'] = True
    output['state'] = reply["state"]
    output['response'] = reply["response"].encode("utf-8")

    return json.dumps(output, indent=4, ensure_ascii=False)
