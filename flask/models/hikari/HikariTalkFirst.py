#-*- coding: utf-8 -*-
# 最初の挨拶を生成するメソッドを定義するファイル

from datetime import datetime
from random import random
import re

from lib.DBController import Ksql

from HikariStatics import pick_random


k = Ksql.Ksql()

def echo_quotation(a, b, c):
    stateLib = []
    stateLib.append("normal") 
    stateLib.append("happy" )
    stateLib.append("angly")
    stateLib.append("doubt")
    stateLib.append("shy")

    bag = {}
    for q in k.select("quotation_talk_first"):
        bag[q[1]] = 1
    output = {}
    reply = pick_random(bag, None, None, None)
    return ["normal", reply]


# =========================================================
# メインの talkFirst 部分
def talkFirst():
    bag = {}
    # 定型句の挨拶
    bag[echo_quotation] = 1

    output = {}
    reply = pick_random(bag, None, None, None)
    output["state"] = reply[0]
    output["response"] = reply[1]

    return output

# =========================================================



if __name__ == "__main__":
    print(echo_quotation())
