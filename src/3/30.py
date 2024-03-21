# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
# 1文を形態素（マッピング型）のリストとして表現せよ．
# 第4章の残りの問題では，ここで作ったプログラムを活用せよ．

import os
import json

with open(os.path.dirname(__file__) + "/neko.txt.mecab", mode="r") as f:
    sentenses = []
    morphemes = []

    for line in f.readlines():
        dict = {}
        list1 = line.split("\t")

        if len(list1) < 2:
            sentenses.append(morphemes)
            morphemes = []
            continue

        surface = list1[0]
        dict["surface"] = surface
        list2 = list1[1].split(",")

        if len(list2) <= 7:
            dict["base"] = list2[0]
        else:
            dict["base"] = list2[7]

        dict["pos"] = list2[0]
        dict["pos1"] = list2[1]

        morphemes.append(dict)

with open(os.path.dirname(__file__) + "/30answer.txt", "w") as f:
    json.dump(sentenses, f)

print(sentenses)
