# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
# その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．
# なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

# この問題以降はvenvを使って進める
# またファイルはwgetで入手しておく
#
# $ source .venv/bin/activate
# $ pip install -r requirements.txt
# $ wget https://nlp100.github.io/data/neko.txt

import os
import MeCab

mecab = MeCab.Tagger()
with open(os.path.dirname(__file__) + "/neko.txt", "r") as in_file:
    with open(os.path.dirname(__file__) + "/neko.txt.mecab", "w") as out_file:
        for line in in_file.readlines():
            result = mecab.parse(line)
            out_file.write(result)
