#-*- coding:utf-8 -*-

from setting import HIKARI_USERNAME as USERNAME
from lib.DBController import Ksql

from hikari_models import HikariReply

import random


# ひかりちゃんAI クラス

agents = {}
talk_log = {}

class Hikari:

    def __init__(self):
        self.user = USERNAME
        self.state = "normal"
        # 以下デバッグ
        self.stateIdx = 0
        self.stateLib = []
        self.stateLib.append("normal")
        self.stateLib.append("happy")
        self.stateLib.append("angly")
        self.stateLib.append("doubt")
        self.stateLib.append("shy")

    def getReply(self, talk_id, query):
        k = Ksql.Ksql()
        if self.stateLib[self.stateIdx] == "normal":
            res = k.select("quotation", where = {"key_id" : "6"})
        else:
            res = k.select("quotation", where = {"match_" + self.stateLib[self.stateIdx] : "1"})
        
        # return "やったね，モデルを経由したよ！"
        return res[0][1]
        # return HikariReply.echo_current_time()

    def changeState(self, talk_id, query):
        
        # self.stateIdx = (self.stateIdx + 1) % len(self.stateLib)
        self.stateIdx = int(random.random() * len(self.stateLib))

        self.state = self.stateLib[self.stateIdx]

        return self.state

    # 引数に入れた文字列を返すだけ．デバッグ用
    def talkEcho(self, query):
        return query

    # start_conversation 時に返す最初の挨拶を生成する
    def talkFirst(self, query):
        return "あ，いらっしゃい．"

if __name__ == "__main__":
    h = Hikari()
    h.talk_log["0000"] = []
    print(h.getReply("0000", "こんにちは"))
