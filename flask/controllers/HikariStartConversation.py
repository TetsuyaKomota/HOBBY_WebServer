#-*-coding: utf-8 -*-

import json

def hikariStartConversation(args, hikariMain):

    # HIKARI の talk_log にエントリーを追加する

    newIdx = len(hikariMain.talk_log)
    while '{0:04d}'.format(newIdx) in hikariMain.talk_log.keys():
        newIdx = newIdx + 1
    newIdx = '{0:04d}'.format(newIdx)

    hikariMain.talk_log[newIdx] = []

    query = ""

    # 最初の挨拶と感情を取得する
    reply = hikariMain.talkFirst(query)

    # 取得した最初の挨拶を talk_log に保持
    hikariMain.talk_log[newIdx].append({"state":reply["state"], "query":query, "response":reply["response"]})

    # return
    output = {}
    output['talk_id'] = newIdx
    output['num_of_talk'] = len(hikariMain.talk_log)
    output['state'] = reply["state"]
    output['response'] = reply["response"].encode("utf-8")

    return json.dumps(output, indent=4, ensure_ascii=False)
