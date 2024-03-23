# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

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
sorted_words = sorted((c.values()), reverse=True)

matplotlib.use('Agg')
plt.xscale('log')
plt.yscale('log')
plt.plot(sorted_words)
plt.savefig(os.path.dirname(__file__) + "/39.png")
