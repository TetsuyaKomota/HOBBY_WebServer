#-*-coding: utf-8 -*-

import json

def hikariEndConversation(args, hikariMain):


    del hikariMain.talk_log[args.get("talk_id", '')]

    output = {}
    output['success'] = True
    output['num_of_talk'] = len(hikariMain.talk_log)
    return json.dumps(output, indent=4, ensure_ascii=False)
