#-*- coding: utf-8 -*-
# 定型句などを生成するメソッドを定義するファイル

from datetime import datetime
from random import random
import re

from lib.DBController import Ksql

from HikariStatics import pick_random
from HikariStatics import getStateLib

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


# 最初に適当に実装してたやつ
def old_getReply(inputs):
        talk_log, state, query = inputs

        stateLib = getStateLib()

        state = int(random() * (len(stateLib)-1)) + 1

        '''
        if state == 1 : #normal
            res = k.select("quotation", where = {"state_key_id" : "1"})
        else:
            res = k.select("quotation", where = {"match_" + state : "1"})
        '''
        res = k.select("quotation", where = {"state_key_id" : str(state)})
        
        return [stateLib[state], res[0][1]]


# ===============================================================

# メインの talk 部分
def talk(talk_log, query):
    state = talk_log[-1]["state"]
    bag = {}
    bag[echo_currentTime] = 1
    bag[echo_randomQuotation] = 1
    bag[old_getReply] = 10

    # 今の時刻を聞かれたら echo_currentTime を実行する    
    if re.search(u"(今|いま)", query) and re.search(u"(何時？)", query):
        bag[echo_currentTime] = bag[echo_currentTime] + 100
    if re.search(u"(時間|じかん)", query):
        bag[echo_currentTime] = bag[echo_currentTime] + 10
   
    output = {}
    reply = pick_random(bag, talk_log, state, query)
    output["state"] = reply[0]
    output["response"] = reply[1]

    return output

# ===============================================================



if __name__ == "__main__":
    print(echo_currentTime())
