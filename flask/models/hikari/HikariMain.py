#-*- coding:utf-8 -*-

from setting import HIKARI_USERNAME as USERNAME
import random

# ひかりちゃんAI クラス

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

    def talk(self, query):
        return "やったね，モデルを経由したよ！"

    def changeState(self, query):
        
        # self.stateIdx = (self.stateIdx + 1) % len(self.stateLib)
        self.stateIdx = int(random.random() * len(self.stateLib))

        self.state = self.stateLib[self.stateIdx]

        return self.state

    # 引数に入れた文字列を返すだけ．デバッグ用
    def talk_echo(self, query):
        return query

if __name__ == "__main__":
    h = Hikari()
    print(h.talk("こんにちは"))
