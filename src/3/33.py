# 2つの名詞が「の」で連結されている名詞句を抽出せよ．

import os
import json

with open(os.path.dirname(__file__) + "/30answer.txt", mode="r") as f:
    sentenses = json.loads(f.read())

list1 = []

for sentense in sentenses:
    for i in range(1, len(sentense)):
        if sentense[i - 1]["pos"] == "名詞" and sentense[i]["surface"] == "の" and sentense[i + 1]["pos"] == "名詞":
            text = str.format(
                "{}の{}",
                sentense[i - 1]["surface"],
                sentense[i + 1]["surface"]
            )

            list1.append(text)

print(list1)
