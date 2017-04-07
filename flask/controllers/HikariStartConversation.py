#-*-coding: utf-8 -*-

import json

def hikariStartConversation(args, hikariMain):


    newIdx = '{0:04d}'.format(len(hikariMain.agents))

    hikariMain.agents[newIdx] = hikariMain.Hikari()

    output = {}
    output['success'] = True
    output['new_idx'] = newIdx
    return json.dumps(output, indent=4, ensure_ascii=False)


