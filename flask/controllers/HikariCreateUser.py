#-*-coding: utf-8 -*-

import json

def hikariCreateUser(form, hikariMain):

    # return
    output = {}
    output['status'] = "OK"
    return json.dumps(output, indent=4, ensure_ascii=False)
