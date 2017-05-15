#-*- coding: utf-8 -*-
# 最初の挨拶を生成するメソッドを定義するファイル

from datetime import datetime
from random import random
import re

from lib.DBController import Ksql

from HikariStatics import pick_random
from HikariStatics import getStateLib


k = Ksql.Ksql()

# pick_random にかける関係上，不要な引数を三つつける必要がある
# TODO どうにかする
def echo_quotation(inputs):
    stateLib = getStateLib()
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
