# coding = utf-8

import dill

# query から想起される word のうち，まだG["nodes"]上で False なものを取得する
def searchstillUnknownRelatedWords(G, query):
    return [e[1] for e in G["edges"] if e[0] == query and G["nodes"][e[1]] == False]

if __name__ == "__main__":
    while True:
        with open("G_CSE.dill", "rb") as f:
            G = dill.load(f)

        print("何について聞きたい？")
        print(">", end="")
        query = input()
        if query == "bye":
            print("じゃーね！")
            break
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
                print("今度調べてみるね！")
                G["nodes"][query] = False
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
