#-*- coding: utf-8 -*-
# 定型句などを生成するメソッドを定義するファイル

from datetime import datetime
from datetime import timedelta
from random import random
import re
from natto import MeCab

from lib.DBController import Ksql

from HikariStatics import pick_random
from HikariStatics import getStateLib
from HikariStatics import echoRandomQuotation

# ===============================================================

# 現在日時をお知らせする
def echo_currentTime(inputs):
    talk_log, state, query = inputs

    # 表情は normal に固定
    # TODO いたるところに state のリテラルをぶち込んでる状態やめたい

    # EC2 上ではなぜか9時間 遅れているようなので，調整
    now = datetime.now() + timedelta(hours=9)
    response = "今は "
    response = response + str(now.month) + "月 "
    response = response + str(now.day) + "日の "
    response = response + str(now.hour) + "時 "
    response = response + str(now.minute) + "分 "
    response = response + "だよ"

    return ["normal", response.decode("utf-8")]

# 名詞について質問する
def ques_noun(inputs):
    talk_log, state, query = inputs
    
    m = MeCab()
    words = m.parse(query.encode("utf-8")).split("\n")
    bag = {}
    for w in words:
        n = w.split(",")
        if len(n) < 2:
            break
        # elif n[0].split("\t")[1] == "名詞" and n[1] != "非自立":
        elif n[0].split("\t")[1] == "名詞" and n[6] == "*":
            if n[0].split("\t")[0] in bag.keys():
                bag[n[0].split("\t")[0]] = bag[n[0].split("\t")[0]] + 1
            else:
                bag[n[0].split("\t")[0]] = 1
        #
    #
    selected = pick_random(bag, None, None, None)
    response = selected + "って何？"
    return ["normal", response.decode("utf-8")]

# ===============================================================

# クエリ内に指定した品詞の単語が存在するか判定する
def hasWordofthisPOS(query, POS):
    m = MeCab()
    words = m.parse(query.encode("utf-8")).split("\n")
    for w in words:
        if len(w.split(",")) < 2:
            break
        if w.split(",")[0].split("\t")[1] == POS:
            return True
        #
    #
    return False

  
# ===============================================================

# メインの talk 部分
def talk(talk_log, query):
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
    # 名詞を見かけたら ques_noun を実行する 
    if hasWordofthisPOS(query, "名詞"):
        quesnoun = quesnoun + 20
    # 何か教えてくれたっぽかったら so_then から乱択する
    if re.search(u"(だよ|それは|事|こと)", query):
        quotationsothen = quotationsothen + 1000
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
