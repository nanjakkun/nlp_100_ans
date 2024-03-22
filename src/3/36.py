# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

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

word_list = []
height_list = []
for i in range(10):
    word_list.append(c.most_common()[:10][i][0])
    height_list.append(c.most_common()[:10][i][1])

# ローカルにファイルで書き出す
# jupiternotebookだとinlineのほうが良いかも
matplotlib.use('Agg')
plt.bar(x=word_list, height=height_list)
plt.savefig(os.path.dirname(__file__) + "/36.png")
