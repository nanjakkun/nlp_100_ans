#!/bin/bash
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．

cat col1.txt | sort | uniq | wc -l
