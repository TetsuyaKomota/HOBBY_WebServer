#-*- coding: utf-8 -*-
# 定型句などを生成するメソッドを定義するファイル

from datetime import datetime
from random import random
import re

from lib.DBController import Ksql

from HikariStatics import pick_random
from HikariStatics import getStateLib
from HikariStatics import echoRandomQuotation

k = Ksql.Ksql()

# MySQL から定型句を取得する
# 引数に表情を受け取り，ランダムに応答を返す
def echo_randomQuotation(inputs):
    talk_log, state, query = inputs
    return [state, u"まだこれしか喋れないよ"]

# 現在日時をお知らせする
def echo_currentTime(inputs):
    talk_log, state, query = inputs

    # 表情は normal に固定
    # TODO いたるところに state のリテラルをぶち込んでる状態やめたい

    now = datetime.now()
    # EC2 上ではなぜか9時間 遅れているようなので，調整
    return ["normal", ("今は " + str(now.month) + "月" + str(now.day) + "日 の " + str((now.hour + 9) % 24) + "時" + str(now.minute) + "分 だよ").decode("utf-8")]

# 感謝されたときにする反応
def echo_forThanks(inputs):
    talk_log, state, query = inputs
    return ["shy", u"お役に立てて良かった良かった！"]

# 最初に適当に実装してたやつ
def old_getReply(inputs):
        talk_log, state, query = inputs
        stateLib = getStateLib()
        
        res = k.selectRandom(u"quotation")
        
        return [stateLib[res[2]], res[1]]


# ===============================================================

# メインの talk 部分
def talk(talk_log, query):
    state = talk_log[-1]["state"]
    bag = {}
    bag[echo_currentTime] = 1
    bag[echo_randomQuotation] = 1
    bag[echo_forThanks] = 1
    bag[echoRandomQuotation(u"quotation")] = 10

    # 今の時刻を聞かれたら echo_currentTime を実行する    
    if re.search(u"(今|いま)", query) and re.search(u"(何時？)", query):
        bag[echo_currentTime] = bag[echo_currentTime] + 100
    if re.search(u"(時間|じかん)", query):
        bag[echo_currentTime] = bag[echo_currentTime] + 10
    # 感謝されたっぽかったら echo_Thanks を実行する
    if re.search(u"(ありがとう|ありがとー|たすかる|たすかった|助かる|助かった)$", query):
        bag[echo_forThanks] = bag[echo_forThanks] + 100
   
    output = {}
    reply = pick_random(bag, talk_log, state, query)
    output["state"] = reply[0]
    output["response"] = reply[1]

    return output

# ===============================================================



if __name__ == "__main__":
    print(echo_currentTime())
