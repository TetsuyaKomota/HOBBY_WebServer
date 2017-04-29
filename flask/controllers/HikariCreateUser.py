#-*-coding: utf-8 -*-

import json

def hikariCreateUser(form, hikariMain):

    # HIKARI の createUser を叩く
    status = hikariMain.createUser(form["user_name"], form["password"])

    # return
    output = {}
    output['result'] = status[0]
    output['message'] = status[1]
    return json.dumps(output, indent=4, ensure_ascii=False)
