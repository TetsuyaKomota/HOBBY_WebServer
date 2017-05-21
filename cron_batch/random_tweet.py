#-*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
from requests_oauthlib import OAuth1Session
from random import random 
import re

from setting import HOSTNAME
from setting import PORT
from setting import HT_API_KEY
from setting import HT_API_SECRET
from setting import HT_ACCESS_KEY
from setting import HT_ACCESS_SECRET

# 適当な確率でツイートする
r = random()
if r < 0.6:
    print("ignored")
    exit()

CK = HT_API_KEY         # Consumer Key
CS = HT_API_SECRET      # Consumer Secret
AT = HT_ACCESS_KEY      # Access Token
AS = HT_ACCESS_SECRET   # Accesss Token Secert

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
now = datetime.now() + timedelta(hours=9)
if now.hour < 4 or now.hour > 18:
# if ((now.hour + 9) % 24) < 4 or ((now.hour + 9) % 24) > 18:
    response = "こんばんは. "
elif now.hour < 11:
# elif ((now.hour + 9) % 24) < 11:
    response = "おはよー. "
else:
    response = "こんにちは. "

response = response + "今は "
response = response + str(now.month) + "月 "
response = response + str(now.day) + "日の "
#response = response + str((now.hour + 9) / 24 + now.day) + "日の "
response = response + str(now.hour) + "時 "
#response = response + str((now.hour + 9) % 24) + "時 "
response = response + str(now.minute) + "分 "
response = response + "だよ"

talkRoomURL = "http://" + HOSTNAME + ":" + str(PORT) + "/talk_room"

response = response + "\n" + talkRoomURL

params = {"status": response}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
    print (req.keys())

# 現在日時をお知らせする
def echo_currentTime(inputs):
    talk_log, state, query = inputs

    # 表情は normal に固定
    # TODO いたるところに state のリテラルをぶち込んでる状態やめたい

    # EC2 上ではなぜか9時間 遅れているようなので，調整
    return ["normal", response.decode("utf-8")]
#
