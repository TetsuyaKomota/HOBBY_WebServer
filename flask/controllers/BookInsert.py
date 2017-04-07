import json
from lib.DBController import Ksql
def bookInsert(args):
    token = Ksql.Ksql()
    token.changeConnection(dbName="PMAN_DB")
    values = {}
    if isinstance(args.get("isbn", ''), str):
        values["isbn"] = args.get("isbn", '').decode("utf-8")
    elif isinstance(args.get("isbn", ''), unicode):
        values["isbn"] = args.get("isbn", '')
 
    if isinstance(args.get("title", ''), str):
        values["title"] = args.get("title", '').decode("utf-8")
    elif isinstance(args.get("title", ''), unicode):
        values["title"] = args.get("title", '')

    if isinstance(args.get("author", ''), str):
        values["author"] = args.get("author", '').decode("utf-8")
    elif isinstance(args.get("author", ''), unicode):
        values["author"] = args.get("author", '')
 


    token.insert(tableName="booklist", values=values)
    output = {}
    output['success'] = True
    return json.dumps(output, indent=4, ensure_ascii=False)


