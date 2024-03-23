# 「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

import os
import json
import matplotlib
import matplotlib.pyplot as plt
import japanize_matplotlib
from functools import reduce

with open(os.path.dirname(__file__) + "/30answer.txt", mode="r") as f:
    sentenses = json.loads(f.read())

dict = {}

for sentense in sentenses:
    neko_exists = any(word["base"] == "猫" for word in sentense)

    if neko_exists:
        for word in sentense:
            if word["base"] != "猫":
                dict[word["base"]] = dict.get(word["base"], 0) + 1

list1 = sorted(dict.items(), key=lambda x: x[1], reverse=True)[0:10]
common_words = list(map(lambda x: x[0], list1))
nums = list(map(lambda x: x[1], list1))

matplotlib.use('Agg')
plt.bar(x=common_words, height=nums)
plt.savefig(os.path.dirname(__file__) + "/37.png")
