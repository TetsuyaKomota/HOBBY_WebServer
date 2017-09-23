# coding = utf-8

import dill
import copy

with open("dills/G_CSE.dill", "rb") as f:
    G = dill.load(f)
    newG = copy.deepcopy(G)

removeList = []
for n in G["nodes"]:
    print(str(n) + " は消しちゃう？")
    flg = False
    while True:
        print("y:消す  n:消さない  e:終了  >", end="")
        print("")
        query = input()
        if query == "e":
            print("了解，じゃあここで終了ね")
            flg = True
            break
        elif query == "y":
            print("了解，消去しまーす")
            removeList.append(n)
            del newG["nodes"][n]
            for e in G["edges"]:
                if n in e:
                    del newG["edges"][e]
            break
        elif query == "n":
            print("了解，じゃあこれは取っておくね")
            break
        else:
            print("え？何？ y か n か e で答えて")
    if flg == True:
        break
    print("")
print("ここまでの編集，セーブしちゃっていい？")
while True:
    print("y:セーブする  n:セーブしない  >", end="")
    print("")
    query = input()
    if query == "y":
        print("了解，じゃあセーブしまーす")
        with open("dills/G_CSE.dill", "wb") as f:
            dill.dump(newG, f)
        print("今回はこれだけのワードを削除したよ")
        print(removeList)
        break
    elif query == "n":
        print("了解，じゃあ編集は破棄しちゃうね")
        break
    else:
        print("y か n で答えてよー")
    print("")
print("はい終了ーまたねー")
