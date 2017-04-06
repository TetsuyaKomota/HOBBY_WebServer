#-*-coding: utf-8 -*-

import json
def hikariTalk(args):
    output = {}
    output['success'] = True
    output['talk'] = "やったね！成功だよ"
    return json.dumps(output, indent=4, ensure_ascii=False)


