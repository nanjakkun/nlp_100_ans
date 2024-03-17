#!/bin/bash
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

echo "Enter number of lines you want to read : "

read n
tail -n ${n} popular-names.txt
