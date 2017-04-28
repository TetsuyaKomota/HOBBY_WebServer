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
    # HIKARI の stateFirst() を叩いて最初の感情を取得する
    initState = hikariMain.stateFirst(query)
    # HIKARI の talkFirst() を叩いて最初の挨拶を取得する
    response = hikariMain.talkFirst(query)
    # 取得した最初の挨拶を talk_log に保持
    hikariMain.talk_log[newIdx].append({"state":initState, "query";query, "response":response})

    # return
    output = {}
    output['talk_id'] = newIdx
    output['num_of_talk'] = len(hikariMain.talk_log)
    output['response'] = response
    return json.dumps(output, indent=4, ensure_ascii=False)


