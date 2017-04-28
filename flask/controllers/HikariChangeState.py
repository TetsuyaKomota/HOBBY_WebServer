#-*-coding: utf-8 -*-

import json
from models.hikari import HikariMain

def hikariChangeState(args, hikariMain):

    talk_id = args.get("talk_id", '')
    query = args.get("query", '')

    state = hikariMain.stateChange(talk_id, query)

    output = {}
    output['success'] = True
    output['state'] = state.encode("utf-8")
    return json.dumps(output, indent=4, ensure_ascii=False)
