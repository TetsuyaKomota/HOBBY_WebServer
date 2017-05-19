#-*- coding: utf-8 -*-
from datetime import datetime
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
now = datetime.now()
if ((now.hour + 9) % 24) < 4 or ((now.hour + 9) % 24) > 18:
    reference = "こんばんは. "
elif ((now.hour + 9) % 24) < 11:
    reference = "おはよー. "
else:
    reference = "こんにちは. "

reference = reference + "今は "
reference = reference + str(now.month) + "月 "
reference = reference + str(now.day) + "日の "
reference = reference + str((now.hour + 9) % 24) + "時 "
reference = reference + str(now.minute) + "分 "
reference = reference + "だよ"

params = {"status": reference}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
    print (req.json())

# 現在日時をお知らせする
def echo_currentTime(inputs):
    talk_log, state, query = inputs

    # 表情は normal に固定
    # TODO いたるところに state のリテラルをぶち込んでる状態やめたい

    # EC2 上ではなぜか9時間 遅れているようなので，調整
    return ["normal", reference.decode("utf-8")]
#
