#!/bin/bash
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

cut -d$'\t' -f 1 popular-names.txt | sort | uniq -c | sort -r
