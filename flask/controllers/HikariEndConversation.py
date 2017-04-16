#-*-coding: utf-8 -*-

import json

def hikariEndConversation(args, hikariMain):


    del hikariMain.agents[args.get("idx", '')]

    output = {}
    output['success'] = True
    output['num_of_agents'] = len(hikariMain.agents)
    return json.dumps(output, indent=4, ensure_ascii=False)
