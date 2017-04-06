#-*- coding:utf-8 -*-

from setting import HIKARI_USERNAME as USERNAME

# ひかりちゃんAI クラス

class Hikari:
    def __init__(self):
       self.user = USERNAME

    def talk(self, query):
        return "やったね，モデルを経由したよ！"

    # 引数に入れた文字列を返すだけ．デバッグ用
    def talk_echo(self, query):
        return query

if __name__ == "__main__":
    h = Hikari()
    print(h.talk("こんにちは"))
