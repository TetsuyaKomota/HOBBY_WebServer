#-*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session

from setting import HT_API_KEY
from setting import HT_API_SECRET
from setting import HT_ACCESS_KEY
from setting import HT_ACCESS_SECRET

CK = HT_API_KEY         # Consumer Key
CS = HT_API_SECRET      # Consumer Secret
AT = HT_ACCESS_KEY      # Access Token
AS = HT_ACCESS_SECRET   # Accesss Token Secert

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
params = {"status": "Hello, World!"}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
