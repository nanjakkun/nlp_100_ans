# 動詞の基本形をすべて抽出せよ．

import os
import json

with open(os.path.dirname(__file__) + "/30answer.txt", mode="r") as f:
    sentenses = json.loads(f.read())

verb_set = set()

for sentense in sentenses:
    for morph in sentense:
        if morph["pos"] == "動詞":
            verb_set.add(morph["base"])

print(verb_set)
