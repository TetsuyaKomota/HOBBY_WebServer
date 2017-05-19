#-*- coding: utf-8 -*-

from random import random

from lib.DBController import Ksql

# HIKARI の主に Talk 関係で使用する汎用メソッドを書いておくところ

# state の dict を取得する
# TODO いつか消す
def getStateLib():
    stateLib = []
    stateLib.append("invalid")
    stateLib.append("normal") 
    stateLib.append("happy" )
    stateLib.append("angly")
    stateLib.append("doubt")
    stateLib.append("shy")
    return stateLib

# state 名から state_key_id を返す
# TODO いつか消す
def getStateKeyId(state):
   if state == u"normal":
        return 1

   if state == u"happy":
        return 2

   if state == u"angly":
        return 3

   if state == u"doubt":
        return 4

   if state == u"shy":
        return 5

# ランダムに一つ選択して文字列を返す関数
    # bag   : dict. 選択肢を key, 比率を value にする
    # query : str.  bag から選択された要素が関数であるならこれを引数に実行した結果を返す．1引数限定
def pick_random(bag, *inputs):
    output = "illigal message"
    total = sum(bag.values())
    count = 0
    rand = total * random()
    for p in bag:
        output = p
        count = count + bag[p]
        if rand < count:
            break
        #
    # 文字列の場合はそのまま出力する
    if type(output) == type("str") or type(output) == type(u"unicode"):
        return output
    # 配列や辞書の場合は第一引数を代入して返す
    elif type(output) == type({"dict":"dict"}) or type(output) == type(["list"]) or type(output) == type(set("set")):
        return output[inputs[0]]
    # 関数の場合は変数を入れて実行する
    else:
        return output(inputs)

# quotation のエントリーを一つ加えると対応する state を返す
def getQuotationState(entry):
    stateLib = getStateLib()
    temp = {}
    temp[1] = entry[2]
    temp[2] = entry[3]
    temp[3] = entry[4]
    temp[4] = entry[5]
    if h==a and a==d and d==s:
        return "normal"
    else:
        return stateLib[max(temp)]

# quotation 系のテーブル名を指定するとランダムで一件取得する
def echoRandomQuotation(tableName):
        k = Ksql.Ksql()
        # テーブル名は quotation 始まり限定
        if tableName.split("_")[0] != u"quotation":
            return None
        else:
            def func(inputs):
                talk_log, state, query = inputs
                stateLib = getStateLib()        
                res = k.selectRandom(tableName)
                return [stateLib[res[2]], res[1]]
            return func


# デバッグ用．
if __name__ == "__main__":
    f = echoRandomQuotation("quotation_talk_first") 
    res = f(({}, 0, u"ほげほげ"))
    for c in res:
        print(c)
'''
def addPrefix(query):
    return("これは"+query)
def hello(query):
    return "こんにちは"
def nest_hello(query):
    return "入れ子からこんにちは"
def nest(query):
    print("この関数は実行されました")
    d = "入れ子"
    e = nest_hello
    bag = {d:6, e:4}
    rep = pick_random(bag, "入れ子関数")
    return rep

if __name__ == "__main__":
    a = "文字列"
    b = addPrefix
    c = hello
    d = nest

    bag = {a:6, b:2, c:1, d:1} 

    itr = 100
    q = "関数"
    t = itr
    na = 0
    nb = 0
    nc = 0
    nd = 0
    ne = 0
    for _ in range(itr):
        rep = pick_random(bag, q)
        if rep == a:
            na = na + 1
        elif rep == b(q):
            nb = nb + 1
        elif rep == c(q):
            nc = nc + 1
        elif rep == "入れ子":
            nd = nd + 1
        elif rep == nest_hello("入れ子関数"):
            ne = ne + 1
        else:
            print("何かおかしい")
            exit()
        #
    #
    print("a:" + str(float(na)/t) + "  b:" + str(float(nb)/t)  + "  c:" + str(float(nc)/t) + "  d:" + str(float(nd)/t)+ "  e:" + str(float(ne)/t))
'''
