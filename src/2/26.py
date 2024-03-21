# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
# （参考: マークアップ早見表）
# https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8

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
        dict[matched.group(1)] = re.sub(r'(\\\'){2,5}', '', matched.group(2))

print(dict)
