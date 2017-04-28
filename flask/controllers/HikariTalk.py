#-*-coding: utf-8 -*-

import json
from models.hikari import HikariMain

def hikariTalk(args, hikariMain):

    talk_id = args.get("talk_id", '')
    query = args.get("query", '')
    # 感情状態の遷移を実行
    state = hikariMain.stateChange(talk_id, query)
    # 返答の取得
    response = hikariMain.getReply(talk_id, query)
    # talk_log に登録
    hikariMain.talk_log[talk_id].append({"state":state, "query":query, "response":response})

    output = {}
    output['success'] = True
    output['response'] = response.encode("utf-8")
    return json.dumps(output, indent=4, ensure_ascii=False)


