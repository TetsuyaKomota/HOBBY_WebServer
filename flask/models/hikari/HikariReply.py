#-*- coding: utf-8 -*-
# 定型句などを生成するメソッドを定義するファイル

from datetime import datetime
from random import random
import re

from lib.DBController import Ksql

from HikariStatics import pick_random
from HikariStatics import getStateLib
from HikariStatics import echoRandomQuotation


# 現在日時をお知らせする
def echo_currentTime(inputs):
    talk_log, state, query = inputs

    # 表情は normal に固定
    # TODO いたるところに state のリテラルをぶち込んでる状態やめたい

    now = datetime.now()
    # EC2 上ではなぜか9時間 遅れているようなので，調整
    reference = "今は "
    reference = reference + str(now.month) + "月 "
    reference = reference + str(now.day) + "日の "
    reference = reference + str((now.hour + 9) % 24) + "時 "
    reference = reference + str(now.minute) + "分 "
    reference = reference + "だよ"

    return ["normal", reference.decode("utf-8")]
# ===============================================================

# メインの talk 部分
def talk(talk_log, query):
    quotation = 10
    curtime = 1
    forthanks = 1
    warningxss = 0

    # 今の時刻を聞かれたら echo_currentTime を実行する    
    if re.search(u"(今|いま)", query) and re.search(u"(何時？)", query):
        curtime = curtime + 100
    if re.search(u"(時間|じかん)", query):
        curtime = curtime + 10
    # 感謝されたっぽかったら echo_Thanks を実行する
    if re.search(u"(ありがとう|ありがとー|たすかる|たすかった|助かる|助かった)$", query):
        forthanks = forthanks + 100
    # <script> タグを発見したら warningXSS を実行する 
    if re.search(u"<script", query):
        warningxss = warningxss + 1000000
 
    state = talk_log[-1]["state"]
    bag = {}
    bag[echo_currentTime] = curtime
    bag[echoRandomQuotation(u"quotation_for_thanks")] = forthanks
    bag[echoRandomQuotation(u"quotation_warning_xss")] = warningxss
    bag[echoRandomQuotation(u"quotation")] = quotation

  
    output = {}
    reply = pick_random(bag, talk_log, state, query)
    output["state"] = reply[0]
    output["response"] = reply[1]

    return output

# ===============================================================



if __name__ == "__main__":
    print(echo_currentTime())
