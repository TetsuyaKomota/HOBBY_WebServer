#-*- coding: utf-8 -*-
# 定型句などを生成するメソッドを定義するファイル

from datetime import datetime
from datetime import timedelta
from random import random
import re
import MeCab

from lib.DBController import Ksql

from HikariStatics import pick_random
from HikariStatics import getStateLib
from HikariStatics import echoRandomQuotation
from HikariStatics import getCurrentTime

# ===============================================================

# 現在日時をお知らせする
def echo_currentTime(inputs):
    talk_log, state, query = inputs

    response = getCurrentTime()
    # 表情は normal に固定
    return ["normal", response]

# 名詞について質問する
def ques_noun(inputs):
    talk_log, state, query = inputs
    
    m = MeCab.Tagger()
    words = m.parse(query).split("\n")
    bag = {"幸せ" : 1}
    for w in words:
        n = w.split(",")
        if len(n) < 2:
            break
        # elif n[0].split("\t")[1] == "名詞" and n[1] != "非自立":
        elif n[0].split("\t")[1] == "名詞" and (n[6] == "*"or n[1] == "固有名詞"):
            if n[0].split("\t")[0] in bag.keys():
                bag[n[0].split("\t")[0]] = bag[n[0].split("\t")[0]] + 1
            else:
                bag[n[0].split("\t")[0]] = 1
        #
    #
    selected = pick_random(bag, None, None, None)
    response = selected + "って何？"
    return ["normal", response]

# ===============================================================

# クエリ内に指定した品詞の単語が存在するか判定する
def hasWordofthisPOS(query, POS, unknown=False):
    m = MeCab.Tagger()
    words = m.parse(query).split("\n")
    for w in words:
        if len(w.split(",")) < 2:
            break
        if w.split(",")[0].split("\t")[1] == POS:
            if unknown != True or w.split(",")[6] == "*":
                return True
        #
    #
    return False
  
# ===============================================================

# メインの talk 部分
def talk(talk_log, query):
    # query の , は全角に変換．（そうしないと MeCab の解析ができない）
    query = re.sub(u",", u"，", query)
    quotation = 10
    quotationsothen = 1
    curtime = 1
    forthanks = 1
    quesnoun = 0
    warningxss = 0

    # 今の時刻を聞かれたら echo_currentTime を実行する    
    if re.search(u"(今|いま)", query) and re.search(u"(何時？)", query):
        curtime = curtime + 100
    if re.search(u"(時間|じかん)", query):
        curtime = curtime + 10
    # 感謝されたっぽかったら echo_Thanks を実行する
    if re.search(u"(ありがとう|ありがとー|たすかる|たすかった|助かる|助かった)$", query):
        forthanks = forthanks + 100
    # 知らない名詞を見かけたら ques_noun を実行する 
    if hasWordofthisPOS(query, "名詞", unknown=True):
        quesnoun = quesnoun + 200
    # 知らなくなくても名詞を見かけたら ques_noun を実行する比率を上げる
    if hasWordofthisPOS(query, "名詞", unknown=False):
        quesnoun = quesnoun + 20
    # 何か教えてくれたっぽかったら so_then から乱択する
    if re.search(u"(だよ|それは|らしい)", query):
        quotationsothen = quotationsothen + 100
    if re.search(u"(こと|事)", query):
        quotationsothen = quotationsothen + 10
    # 直前に「～って何？」って聞いてたら相槌の確率を上げる
    if re.search(u"(って何)", talk_log[-1]["response"]):
        quotationsothen = quotationsothen + 20
    # <script> タグを発見したら warningXSS を実行する 
    if re.search(u"<script", query):
        warningxss = warningxss + 1000000
 
    state = talk_log[-1]["state"]
    bag = {}
    bag[echo_currentTime] = curtime
    bag[ques_noun] = quesnoun
    bag[echoRandomQuotation(u"quotation_for_thanks")] = forthanks
    bag[echoRandomQuotation(u"quotation_warning_xss")] = warningxss
    bag[echoRandomQuotation(u"quotation")] = quotation
    bag[echoRandomQuotation(u"quotation_so_then")] = quotationsothen

  
    output = {}
    reply = pick_random(bag, talk_log, state, query)
    output["state"] = reply[0]
    output["response"] = reply[1]

    return output

# ===============================================================



if __name__ == "__main__":
    # print(echo_currentTime())
    print(talk([{"state": 1}], u"今日もまた人が死んだよ．俺はこうして生きているのに．起き抜けにあの夢を見たんだ．どんな夢かは言えないけれど")["response"])
