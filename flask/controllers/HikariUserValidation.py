#-*-coding: utf-8 -*-

import json

def hikariUserValidation(request, hikariMain):

    # HIKARI の isValidUserName を叩く
    status = hikariMain.isValidUserName(request.form["user_name"])

    # return
    output = {}
    output['status'] = status[0]
    output['message'] = status[1]
    return json.dumps(output, indent=4, ensure_ascii=False)


