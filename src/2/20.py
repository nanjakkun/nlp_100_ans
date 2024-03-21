# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

import json

with open("jawiki-country.json", mode="r") as f:
  for line in f:
    obj = json.loads(line)
    if obj['title'] == 'イギリス':
      text = obj['text']
      print(text)
      break
