#-*- coding: utf-8 -*-

import dill
import numpy as np
import unicodedata
from random import random
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

from HikariStatics import getCSEDict
from HikariStatics import isValidCharType
from natto import MeCab

from lib.DBController import Ksql

k = Ksql.Ksql()

# TFIDF を用いて単語の関係を学習する

# talk_log から適当に検索するワードを取得
def getUnknownWord():
    unknownword = ""
    for _ in range(500):
        query = k.selectRandom("talk_log")[3]
        m = MeCab()
        print("実行前 : " + query.encode("utf-8"))
        query_wakati = m.parse(query.encode("utf-8")).split("\n")
        unknownword = ""
        flg = False
        for q in query_wakati:
            temp = q.split(",")
            if len(temp) < 2:
                break
            # 不必要なところで分かち書きしてるかもしれないので，
            # 
            if temp[6] == "*":
                # 微妙にランダム性を持たせる
                if flg == False and random() > 0.25:
                    continue
                flg = True
                unknownword = unknownword + temp[0].split("\t")[0]
            elif flg == True:
                break
        if len(unknownword) < 2:
            continue
        entries = k.select("knowledge_related_word", where={"query":unknownword.decode("utf-8")})
        # knowledge テーブルにないワードの場合，それを返す
        if len(entries) == 0:
            return unknownword
    return ""        

# 取得してきた辞書から，名詞をカウントする
def countingNoun(dic):
    m = MeCab()
    count = {}
    for d in dic:
        # getCSEDict で取得した単語集は空白区切りになっているはずなので，空白で split
        words = dic[d].split(" ")
        for w in words:
            if len(m.parse(w).split(",")) < 2:
                break
            # 名詞以外は無視
            if m.parse(w).split(",")[0].split("\t")[1] != "名詞":
                continue
            if w in count.keys():
                count[w] = count[w] + 1
            else:
                count[w] = 1
            #
        #
    #
    return count

# TFIDF の最大値が低い単語のリストを生成する
def selectWordswithTFIDF(dic):
    if len(dic) < 2:
        return []

    output = []

    count = CountVectorizer()
    bag = count.fit_transform(np.array(dic.values()))
    tfidf = TfidfTransformer(use_idf = True, norm = "l2", smooth_idf = True)
    bag_tfidf = tfidf.fit_transform(bag)

    for idx in range(len(bag_tfidf.toarray().T)):
        pick = bag_tfidf.toarray().T[idx].max()
        if pick < 0.25:
            for name, i in count.vocabulary_.items():
                if idx == i:
                    output.append(name.encode("utf-8"))
                    break
                #
            #
        #
    #
    return output

# 

if __name__ == "__main__":
   
    query = getUnknownWord() 
    print("実行後 : " + query)
    if query == "":
        exit()
    dic = getCSEDict(query, 10)
    '''
    with open("gomi.dill", "wb") as f:
        dill.dump(dic, f)
    with open("gomi.dill", "rb") as f:
    '''
    if True:
        dic = dill.load(f)
        remdic = selectWordswithTFIDF(dic)
        count = countingNoun(dic)
        sumnoun = sum(count.values())
        print(sumnoun)
        for c in count:
            if count[c] > (sumnoun*0.005) and c not in remdic and isValidCharType(c):
                print(c + ":" + str(count[c]) + " : " + unicodedata.name(c.decode("utf-8")[0]))
                k.insert("knowledge_related_word", values={"query" : query.decode("utf-8"), "related_word" : c.decode("utf-8")})
