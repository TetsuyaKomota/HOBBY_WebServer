#-*-coding: utf-8 -*-

import json

def hikariLogin(form, hikariMain):

    # return
    output = {}
    output['result'] = "OK, Login!"
    return json.dumps(output, indent=4, ensure_ascii=False)
