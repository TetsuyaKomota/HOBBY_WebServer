#-*-coding: utf-8 -*-

import json

def hikariCreateUser(request, hikariMain):

    # HIKARI の createUser を叩く
    status = hikariMain.createUser(request.form["user_name"], request.form["password"])

    # return
    output = {}
    output['result'] = status[0]
    output['message'] = status[1]
    return json.dumps(output, indent=4, ensure_ascii=False)
