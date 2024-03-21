# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．

import os
import re

# 20番の問題を解いてtxtファイルを予め作成しておく必要がある
with open(os.path.dirname(__file__) + "/20answer.txt", mode="r") as f:
    text = f.read()

pattern = re.compile(r'基礎情報(.*)\<references/\>', re.MULTILINE | re.DOTALL)
extracted = re.findall(pattern, text)

dict = {}

for row in extracted[0].split("\n"):
    matched = re.match(r"\|([^=\s]+)\s*=\s*(.*)", row)

    if (matched):
        replaced = re.sub(r'(\[\[|\]\]|{{|}})', '', re.sub(
            r'(\\\'){2,5}', '', matched.group(2)))
        dict[matched.group(1)] = replaced

print(dict)
