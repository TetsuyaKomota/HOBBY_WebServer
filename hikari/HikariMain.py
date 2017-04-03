#-*- coding:utf-8 -*-

from setting import HIKARI_USERNAME as USERNAME

# ひかりちゃんAI クラス

class Hikari:
    def __init__(self):
       self.user = USERNAME

    def talk(self, querry):
        return "いや，意味わかんないよ"+USERNAME


if __name__ == "__main__":
    h = Hikari()
    print(h.talk("こんにちは"))
