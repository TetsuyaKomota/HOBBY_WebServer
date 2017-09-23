# coding = utf-8

import dill

G = {"nodes":{}, "edges":{}}
G["nodes"]["けものフレンズ"] = False

with open("dills/newG_CSE.dill", "wb") as f:
    dill.dump(G, f)

