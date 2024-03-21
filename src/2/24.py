# 記事から参照されているメディアファイルをすべて抜き出せ．

import os
import re

# 20番の問題を解いてtxtファイルを予め作成しておく必要がある
with open(os.path.dirname(__file__) + "/20answer.txt", mode="r") as f:
    text = f.read()

extracted = re.findall(r"ファイル:([^|]*)", text)

print(extracted)
