#-*-coding: utf-8 -*-

import json
from models.hikari import HikariMain

def hikariChangeState(args, h):

    # h = HikariMain.Hikari()

    output = {}
    output['success'] = True
    output['state'] = h.changeState(args.get("query", '')).encode("utf-8")
    return json.dumps(output, indent=4, ensure_ascii=False)
