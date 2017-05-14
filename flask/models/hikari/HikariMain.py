#-*- coding:utf-8 -*-

import random
import unicodedata

from setting import HIKARI_USERNAME as USERNAME
from setting import HIKARI_MAX_USER_NAME_LENGTH, HIKARI_VALID_CHAR_TYPE
from lib.DBController import Ksql

import HikariReply


# ひかりちゃんAI クラス


class Hikari:

    def __init__(self):
        self.user = USERNAME
        self.state = "normal"
        self.talk_log = {}
        # 以下デバッグ
        self.stateIdx = 0
        self.stateLib = []
        self.stateLib.append("normal")
        self.stateLib.append("happy")
        self.stateLib.append("angly")
        self.stateLib.append("doubt")
        self.stateLib.append("shy")


    # ユーザー名のバリデーション処理
    def isValidUserName(self, name):
        result = True
        message = ""
        # ユーザー名が空でないか
        if len(name) == 0:
            result = False
            message = "void name."
        # 不適切な文字が含まれていないか
        elif self.isValidCharType(name)  == False:
            result = False
            message = "include invalid charactor."
        # ユーザー名の長さが適切か
        elif len(name) > HIKARI_MAX_USER_NAME_LENGTH:
            result = False
            message = "too long."
        # 既に存在する名前でないか
        elif self.isNewUserName(name) == False:
            result = False
            message = "already exist."
           
        return [result, message]

    # 使用不可能な文字タイプかないかどうか判定する
    def isValidCharType(self, text):
        result = True
        if isinstance(text, unicode) == True:
            t = text
        else:
            t = text.decode("utf-8")
        for char in t:
            charType = unicodedata.name(char).split(" ")[0]
            if charType in ["FULLWIDTH", "HALFWIDTH"]:
                charType = unicodedata.name(char).split(" ")[1]
            if (charType in HIKARI_VALID_CHAR_TYPE) == False:
                result = False
                break
        return result
    # 既に存在するユーザーでないか判定する
    def isNewUserName(self, name):
        result = True
        k = Ksql.Ksql()
        users = []
        if isinstance(name, unicode) == True:
            n = name
        else:
            n = name.decode("utf-8")
        #
        for e in k.select(u"user", select = {u"user_name":0}):
            users.append(e[0])
        if n in users:
            result = False
        return result 

    # 新規登録
    def createUser(self, userName, password):
        result = True
        message = ""
        # 最後にもう一度バリデーションを通す
        status = self.isValidUserName(userName)
        if status[0] == False:
            result = status[0]
            message = status[1]
        else:
            k = Ksql.Ksql()
            k.insert(u"user", values = {u"user_name" : userName, u"password" : password})
        return [result, message]

    # ログイン
    def login(self, userName, password):
        result = True
        message = ""
        # user テーブルに存在する名前か確認する
        if self.isNewUserName(userName) == True:
            result = False
            message = "userName or password is/are wrong..."
        else:
            c = self.isCollectPassword(userName, password)
            if c[0] == False:
                result = False
                message = "userName or password is/are wrong..."
            else:
                message = str(c[1])
        return [result, message]   
 
    # 指定したユーザーのパスワードが正しいか判定. 正しい場合は id を一緒に送る
    def isCollectPassword(self, userName, password):
        result = True
        userId = -1
        k = Ksql.Ksql()
        if isinstance(userName, unicode) == True:
            n = userName
        else:
            n = userName.decode("utf-8")
        user = k.select(u"user", where={u"user_name" : n, u"password" : password})
        if len(user) != 1:
            result = False
        else:
            userId = user[0][0]
        return [result, userId]
# =================================================================================================================
# state 関係メソッド
    # start_conversation 時に決定する最初の感情を生成する
    def stateFirst(self, query):
        self.state = "normal"
        return self.state

    def stateChange(self, talk_id, query):
        
        # self.stateIdx = (self.stateIdx + 1) % len(self.stateLib)
        self.stateIdx = int(random.random() * len(self.stateLib))

        self.state = self.stateLib[self.stateIdx]

        return self.state

# =================================================================================================================
# talk 関係メソッド
   # start_conversation 時に返す最初の挨拶を生成する
    def talkFirst(self, query):
        return "あ，いらっしゃい．"

    def getReply(self, talk_id, query):
        return HikariReply.talk(self.talk_log[talk_id], self.state, query)

    # 引数に入れた文字列を返すだけ．デバッグ用
    def talkEcho(self, query):
        return query

if __name__ == "__main__":
    h = Hikari()
    # h.self.talk_log["0000"] = []
    # print(h.getReply("0000", "こんにちは"))
    print(h.isValidUserName("takeshi"))
    print(h.isValidUserName("さとし"))
    print(h.isValidUserName("つぎは？"))
    print(h.isValidUserName("masa@横浜"))
    # print(h.createUser(u"シゲル","3141592653"))
