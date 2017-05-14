#-*- coding: utf-8 -*-
# 定型句などを生成するメソッドを定義するファイル

from lib.DBController import Ksql

from datetime import datetime

k = Ksql.Ksql()

# MySQL から定型句を取得する
# 引数に表情を受け取り，ランダムに応答を返す
def echo_random_quotation(state):
    
    return "まだこれしか喋れないよ"

# 現在日時をお知らせする
def echo_current_time():

    now = datetime.now()
    # EC2 上ではなぜか9時間 遅れているようなので，調整
    return ("今は " + str(now.month) + "月" + str(now.day) + "日 の " + str((now.hour + 9) % 24) + "時" + str(now.minute) + "分 だよ").decode("utf-8")


# 最初に適当に実装してたやつ
def old_getReply(talk_log, state, query):
        k = Ksql.Ksql()

        stateIdx = 0
        stateLib = {}
        stateLib["normal"] = 0
        stateLib["happy"] = 1
        stateLib["angly"] = 2
        stateLib["doubt"] = 3
        stateLib["shy"] = 4

        if stateLib[state] == 0:
            res = k.select("quotation", where = {"key_id" : "6"})
        else:
            res = k.select("quotation", where = {"match_" + state : "1"})
        
        return res[0][1]


# ===============================================================

# メインの talk 部分
def talk(talk_log, state, query):
    return old_getReply(talk_log, state, query)

# ===============================================================



if __name__ == "__main__":
    print(echo_current_time())
