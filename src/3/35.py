# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

import os
import json
import collections
from functools import reduce

with open(os.path.dirname(__file__) + "/30answer.txt", mode="r") as f:
    sentenses = json.loads(f.read())


def flatten(xs):
    return reduce(lambda a, b: a + b, xs)


def get_base(x):
    return x["base"] if x["pos"] != "補助記号" else None


words = filter(None, map(get_base, flatten(sentenses)))

c = collections.Counter(words)
print(c.most_common())
