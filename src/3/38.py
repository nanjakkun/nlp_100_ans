# 単語の出現頻度のヒストグラムを描け．
# ただし，横軸は出現頻度を表し，1から単語の出現頻度の最大値までの線形目盛とする．
# 縦軸はx軸で示される出現頻度となった単語の異なり数（種類数）である．

import os
import json
import collections
import matplotlib
import matplotlib.pyplot as plt
import japanize_matplotlib
from functools import reduce

with open(os.path.dirname(__file__) + "/30answer.txt", mode="r") as f:
    sentenses = json.loads(f.read())


def flatten(xs):
    return reduce(lambda a, b: a + b, xs)


def get_base(x):
    return x["base"] if x["pos"] != "補助記号" else None


words = filter(None, map(get_base, flatten(sentenses)))
c = collections.Counter(words)

matplotlib.use('Agg')
plt.hist(c.values(), 50, range=(1, 50))
plt.savefig(os.path.dirname(__file__) + "/38.png")
