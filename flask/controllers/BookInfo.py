import json
import datetime
from models import RakutenBookInfo

def bookInfo(args):
    output = {}
    output['success'] = True
    bookInfo = RakutenBookInfo.Api_getBookInfo(args.get("isbn", ""), datetime.date.today().isoformat())
    output['bodydata'] = bookInfo["bodydata"]
    output['isbn'] = bookInfo["isbn"]
    output['title'] = bookInfo["title"]
    output['author'] = bookInfo["author"]
    return json.dumps(output, indent=4, ensure_ascii=False)


