# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

import os
import json

with open(os.path.dirname(__file__) + "/30answer.txt", mode="r") as f:
    sentenses = json.loads(f.read())

list1 = []
for sentense in sentenses:
    i = 0
    while i < len(sentense):
        if sentense[i]["pos"] == "名詞":
            list2 = [sentense[i]["surface"]]

            cnt = 1
            for j in range(1, len(sentense)):
                if sentense[i + j]["pos"] == "名詞":
                    list2.append(sentense[i + j]["surface"])
                    cnt += 1
                else:
                    break

            if len(list2) > 2:
                list1.append("".join(list2))

        i += cnt

print(list1)
