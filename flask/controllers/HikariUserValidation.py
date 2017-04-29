#-*-coding: utf-8 -*-

import json

def hikariUserValidation(form, hikariMain):

    # HIKARI の isValidUserName を叩く
    status = hikariMain.isValidUserName(form["user_name"])

    # return
    output = {}
    output['status'] = status.result
    output['message'] = status.message
    return json.dumps(output, indent=4, ensure_ascii=False)


