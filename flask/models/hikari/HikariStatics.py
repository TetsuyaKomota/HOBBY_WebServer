#-*- coding: utf-8 -*-
import requests
import urllib
import dill
import re
from random import random
from natto import MeCab

from lib.DBController import Ksql
from setting import CSE_API_KEY
from setting import CSE_SEARCH_ENGINE_ID

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

# Google Custom Search API を用いて記事を検索し，記事のタイトルをキー，内容を値とした辞書を返す
def getCSEDict(query, numofArticles):
    url = "https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&q=%s&num=%s"
    url = url % (CSE_API_KEY, CSE_SEARCH_ENGINE_ID, urllib.quote(query), str(numofArticles))
    # API をリクエスト
    res = requests.get(url)
    # レスポンスから単語の辞書を作る
    articles = {}
    for i in res.json()["items"] :
        # URL から HTML を取得する
        html = requests.get(i["link"]).text
        # いろいろ整理する．タグと関数っぽいところを消す
        html = re.sub("<[\d\D]*?>", "", html)
        html = re.sub("{[\d\D]*?}", "", html)
        # 改行とタブを消す
        html = re.sub("(\n|\t)", " ", html)
        # カンマを消す
        html = re.sub(",", " ", html)
        # 空白を減らす
        html = re.sub("( |　)+", " ", html)
        # 形態素解析を行う
        m = MeCab()
        html_wakati = m.parse(html.encode("utf-8")).split("\n")
        words = ""
        for w in html_wakati:
            temp = w.split(",")
            if len(temp) < 2:
                break
            # 名詞，動詞，形容詞以外は無視
            if len(temp[0].split("\t")) < 2 or temp[0].split("\t")[1] not in ("名詞", "動詞", "形容詞"):
                continue
            if temp[6] != "*":
                tempword = temp[6]
            else:
                tempword = temp[0].split("\t")[0]
            # 英単語を無視する
            # TODO これでいいか考える
            if tempword == tempword.decode("utf-8"):
                continue
            # 追加する
            words = words + tempword + " "
        articles[i["title"]] = words
    return articles

# デバッグ用．
if __name__ == "__main__":
    '''
    f = echoRandomQuotation("quotation_talk_first") 
    res = f(({}, 0, u"ほげほげ"))
    for c in res:
        print(c)
    '''
    dic = getCSEDict("けものフレンズ", 10)
    for d in dic:
        print(d)
        print(dic[d])
    print(len(dic))
