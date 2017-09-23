# coding = utf-8

import urllib.parse
import requests
import MeCab
import dill
import re
from random import random
import numpy as np
from setting import CSE_API_KEY
from setting import CSE_SEARCH_ENGINE_ID
from setting import HT_NUM_OF_CANDIDATE
from setting import HT_NUM_OF_SELECTION

# Google Custom Search API を用いて記事を検索し，取得する
def getCSEArticles(query, numofArticles):
    url = "https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&q=%s&num=%s"
    url = url % (CSE_API_KEY, CSE_SEARCH_ENGINE_ID, urllib.parse.quote(query), str(numofArticles))
    # API をリクエスト
    res = requests.get(url)
    return res    

# query から想起される word のうち，まだG["nodes"]上で False なものを取得する
def searchstillUnknownRelatedWords(G, query):
    return [e[1] for e in G["edges"] if e[0] == query and G["nodes"][e[1]] == False]

if __name__ == "__main__":

    m = MeCab.Tagger()
    query = "けものフレンズ"
    for _ in range(50):
        # 現時点での学習済みグラフを読み込み
        with open("G_CSE.dill", "rb") as f:
            G = dill.load(f)
        print("current G:")
        print("Node:")
        print(G["nodes"].keys())
        print("Edge:")
        for e in G["edges"]:
            print(str(e) + ":" + str(G["edges"][e]))
 
        # 検索する query を選択
        # G の nodes に属するもののうち．まだ検索していないもの
        """
        kemono = searchstillUnknownRelatedWords(G, "けものフレンズ")
        if all([G["nodes"][k] for k in kemono]) == True:
            print("すべてのワードが既に検索済みです")
            exit()
        """
        while True:
            query = np.random.choice(list(G["nodes"].keys()))
            # query = np.random.choice(list(kemono))
            if G["nodes"][query] == False:
                break
        
        print("search related words of "+query)
        res = getCSEArticles(query, 10)
        if "items" not in res.json().keys():
            print(res.json())
            exit()
        articles = {}
        for item in res.json()["items"]:
            html = requests.get(item["link"]).text
            # いろいろ整理する．タグと関数っぽいところを消す
            html = re.sub("<[\d\D]*?>", "", html)
            html = re.sub("{[\d\D]*?}", "", html)
            # 改行とタブを消す
            html = re.sub("(\n|\t)", " ", html)
            # カンマを消す
            html = re.sub(",", " ", html)
            # 空白を減らす
            html = re.sub("( |　)+", " ", html)
            # 形態素解析を行う
            html_wakati = m.parse(html).split("\n")
            words = {}
            concat = ""
            catflg = False
            for w in html_wakati:
                temp = w.split(",")
                if len(temp) < 2:
                    break
                # 名詞以外は無視
                if len(temp[0].split("\t")) < 2 or temp[0].split("\t")[1] not in ("名詞"):
                    if catflg == False:
                        continue
                    else:
                        tempword = concat
                        concat = ""
                        catflg = False
                else:
                    if temp[6] != "*":
                        tempword = temp[6]
                    else:
                        tempword = temp[0].split("\t")[0]
                    if concat != "":
                        catflg = True
                    concat += tempword
                # 英単語を無視する
                tempFlg = False
                for t in tempword:
                    # ASCII 上で 32~127 は 半角文字を表すらしい
                    # http://qiita.com/kakk_a/items/3aef4458ed2269a59d63
                    if t in [chr(c) for c in range(32, 127)]:
                        tempFlg = True
                        break
                # 一文字でも半角英数なら英単語だと判定する
                if tempFlg == True:
                    continue
                # 短すぎる単語は無視する
                if len(tempword) <= 2:
                    continue
                # 追加する
                if tempword in words.keys():
                    words[tempword] += 1
                else:
                    words[tempword] = 1
            articles[item["title"]] = words
        relatedWords = {}
        # 検索済みのページ数
        # 名詞種類数が numofCandidate 未満のページ分は除外
        numofpages = 10
        for a in articles:
            # print("---"+a+"---")
            s = sorted(articles[a].items(), key=lambda x: x[1])
            # print(s)
            numofCandidate = HT_NUM_OF_CANDIDATE
            if len(s) < numofCandidate:
                # print("nothing...")
                numofpages -= 1
                continue
            for i in range(numofCandidate):
                # print(s[-i-1][0] + "\t:" + str(s[-i-1][1]))
                if s[-i-1][0] in relatedWords.keys():
                    relatedWords[s[-i-1][0]] += 1
                else:
                    relatedWords[s[-i-1][0]] = 1
        # relatedWords に属するすべての word は語彙として G に保存
        # その中で上位 numofSelection に属する word に関しては
        # query に対する距離を計算する
        nodes = list(G["nodes"])+list(relatedWords.keys())
        nodes_dict = {}
        for n in nodes:
            if n not in G["nodes"].keys():
                nodes_dict[n] = False
            else:
                nodes_dict[n] = G["nodes"][n]
        G["nodes"] = nodes_dict

        print("---Related Words---")
        s = sorted(relatedWords.items(), key=lambda x: x[1])
        nextQuery = ""
        sumS = sum([t[1] for t in s])
        sigma = 0
        numofSelection = HT_NUM_OF_SELECTION
        if len(s) < numofSelection:
            print("nothing...")
        for i in range(numofSelection):
            print(s[-i-1][0] + "\t:" + str(s[-i-1][1]))
            if (query, s[-i-1][0]) not in G["edges"].keys():
                G["edges"][(query, s[-i-1][0])] = numofpages/s[-i-1][1]
            else:
                G["edges"][(query, s[-i-1][0])] += numofpages/s[-i-1][1]
                G["edges"][(query, s[-i-1][0])] /= 2
        # 保存する
        with open("G_CSE.dill", "wb") as f:
            dill.dump(G, f)
