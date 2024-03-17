#!/bin/bash
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

echo "Enter number of lines you want to read : "

read n
head -n ${n} popular-names.txt
