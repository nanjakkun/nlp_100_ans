#!/bin/bash
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

echo "Enter number of lines you want to read : "

read n
split -n ${n} -d --additional-suffix=.txt popular-names.txt .
