#-*- coding: utf-8 -*-

from random import random

# HIKARI の主に Talk 関係で使用する汎用メソッドを書いておくところ

# ランダムに一つ選択して文字列を返す関数
    # bag   : dict. 選択肢を key, 比率を value にする
    # query : str.  bag から選択された要素が関数であるならこれを引数に実行した結果を返す．1引数限定
def pick_random(bag, talk_log, state, query):
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
    #
    if type(output) == type("str") or type(output) == type(u"unicode"):
        return output
    else:
        return output(talk_log, state, query)


# デバッグ用．
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
