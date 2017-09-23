# coding = utf-8

import dill
import copy
import unicodedata

with open("dills/G_CSE.dill", "rb") as f:
    G = dill.load(f)
    newG = copy.deepcopy(G)

removeList = []
validList = ["HIRAGANA", "KATAKANA", "CJK"]
for n in G["nodes"]:
        flg = False
        for t in n:
            # 伸ばし棒は許容
            if t == "ー":
                continue
            if unicodedata.name(t).split(" ")[0] not in validList:
                flg = True
                break
        if flg == True:
            removeList.append(n)
            del newG["nodes"][n]
            for e in G["edges"]:
                if n in e and e in newG["edges"].keys():
                    del newG["edges"][e]

print("この辺全部消しちゃっても大丈夫かな？")
print(removeList)
while True:
    print("y:消してOK  n:消しちゃダメ  >", end="")
    query = input()
    print("")
    if query == "y":
        print("了解，じゃあ全部消してセーブしまーす")
        with open("dills/G_CSE.dill", "wb") as f:
            dill.dump(newG, f)
        break
    elif query == "n":
        print("了解，じゃあ編集は破棄しちゃうね")
        break
    else:
        print("y か n で答えてよー")
    print("")
print("はい終了―．またねー")
