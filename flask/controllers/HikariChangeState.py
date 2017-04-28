#-*-coding: utf-8 -*-

import json
from models.hikari import HikariMain

def hikariChangeState(args, hikariMain):

    # h = HikariMain.Hikari()

    h = hikariMain.agents[args.get("idx", '')]

    output = {}
    output['success'] = True
    output['state'] = h.stateChange(args.get("query", '')).encode("utf-8")
    return json.dumps(output, indent=4, ensure_ascii=False)
