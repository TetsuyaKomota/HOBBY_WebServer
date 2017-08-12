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

from HikariStatics import pick_random

# 適当な確率でツイートする
r = random()
if r < 0.4:
    print("ignored")
    exit()

CK = HT_API_KEY         # Consumer Key
CS = HT_API_SECRET      # Consumer Secret
AT = HT_ACCESS_KEY      # Access Token
AS = HT_ACCESS_SECRET   # Accesss Token Secert

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文

bag = {
    "少しずつだけど，みんなの言ってくれることを理解しようと頑張ってるよ！\n暇なときにでも，話しかけてみてほしいな！" : 1
}

response = pick_random(bag)

# talkRoomURL = "http://" + HOSTNAME + ":" + str(PORT) + "/talk_room"
talkRoomURL = "http://" + HOSTNAME + "/talk_room"

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
