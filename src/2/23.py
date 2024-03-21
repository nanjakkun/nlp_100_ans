# 記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．
#
# https://ja.wikipedia.org/wiki/Help:%E3%82%BB%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3

import os
import re

# 20番の問題を解いてtxtファイルを予め作成しておく必要がある
with open(os.path.dirname(__file__) + "/20answer.txt", mode="r") as f:
    text = f.read()

extracted = re.findall(r"(={2,4}.*)", text)

for row in extracted:
    matched = re.match(r"(=+)([^=]+)", row)
    print(matched.group(2))
    print(len(matched.group(1)))
