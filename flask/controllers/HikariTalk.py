#-*-coding: utf-8 -*-

import json
from models.hikari import HikariMain

def hikariTalk(args):

    h = HikariMain.Hikari()

    output = {}
    output['success'] = True
    output['talk'] = 'やったね，' + h.talk_echo(args.get("query", '')).encode("utf-8")
    return json.dumps(output, indent=4, ensure_ascii=False)


