# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

import os
import re

# 20番の問題を解いてtxtファイルを予め作成しておく必要がある
with open(os.path.dirname(__file__) + "/20answer.txt", mode="r") as f:
    text = f.read()

pattern = re.compile(r'基礎情報(.*)\<references/\>', re.MULTILINE | re.DOTALL)
extracted = re.findall(pattern, text)

dict = {}

for row in extracted[0].split("\n"):
    # ex. '|略名  =イギリス'
    matched = re.match(r"\|([^=\s]+)\s*=\s*(.*)", row)

    if (matched):
        dict[matched.group(1)] = matched.group(2)

print(dict)
