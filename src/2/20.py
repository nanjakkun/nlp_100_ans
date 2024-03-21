# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

import json
import os

text = ""

with open(os.path.dirname(__file__) + "/jawiki-country.json", mode="r") as f:
    for line in f:
        obj = json.loads(line)
        if obj['title'] == 'イギリス':
            text = obj['text']
            break

with open(os.path.dirname(__file__) + "/20answer.txt", "w") as f:
    f.write(text)

print(text)
