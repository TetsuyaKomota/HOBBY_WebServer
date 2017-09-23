# coding = utf-8

import dill

# query から想起される word のうち，まだG["nodes"]上で False なものを取得する
def searchstillUnknownRelatedWords(G, query):
    return [e[1] for e in G["edges"] if e[0] == query and G["nodes"][e[1]] == False]

if __name__ == "__main__":
    while True:
        with open("dills/G_CSE.dill", "rb") as f:
            G = dill.load(f)

        print("何について聞きたい？")
        print(">", end="")
        query = input()
        if query == "bye":
            print("じゃーね！")
            break
        elif query == "nodes":
            print("今は" + str(len(G["nodes"])) + " 単語を知ってるよ！")
        elif query == "knowns":
            print("今までで " + str(len([a for a in G["nodes"] if G["nodes"][a] == True])) + " 単語について調べたよ！")
        elif query == "linkhist":
            print("ノードごとの接続リンク数のヒストグラムを調べてみるよ！")
            hist = {}
            for n in G["nodes"]:
                count = len([e for e in G["edges"].keys() if e[0] == n])
                if count not in hist.keys():
                    hist[count] = [1, n]
                else:
                    hist[count][0] += 1
                    if len(hist[count]) < 4:
                        hist[count].append(n)
                    elif len(hist[count]) == 4:
                        hist[count].append("...")
            print("こんな感じだよ！")
            for h in sorted(list(hist.keys())):
                print(str(h) + ":" + str(hist[h]))
        elif query[:5] == "unk->":
            unk = searchstillUnknownRelatedWords(G, query.split("->")[1])
            if len(unk) == 0:
                print("それはまだ調べてないんだよね")
            else:
                print("これとかかなぁ")
                for u in unk:
                    print(u)
        elif query not in G["nodes"]:
            print("ごめん，それは知らないなぁ...")
            if len(query) >= 4:
                print("調べるリストに入れておいた方がいい？ Y or n")
                while True:
                    print(">", end="")
                    rep = input()
                    if rep not in ["Y", "n"]:
                        print("ん？どっち？ Y か n で答えてよ")
                        continue
                    elif rep == "Y":
                        print("了解！いつか調べるね！")
                        G["nodes"][query] = False
                    else:
                        print("了解！じゃあもう忘れちゃうね！")
                    break
        else:
            rel = {}
            for e in G["edges"]:
                if query in e and e[0] != e[1]:
                    rel[[E for E in e if E != query][0]] = G["edges"][e]

            s = sorted(rel.items(), key=lambda x: x[1])
            size = min(len(s), 3)
            print("それは知ってるよ！これと関係あるでしょ？")
            for i in range(size):
                print(s[-i-1][0])
        with open("G_CSE.dill", "wb") as f:
            dill.dump(G, f)
        print("\n次は", end="")
