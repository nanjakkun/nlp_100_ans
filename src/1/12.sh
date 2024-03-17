#!/bin/bash
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

cat popular-names.txt | sed 's/\t/ /g' | cut -f 1 -d " " > col1.txt
cat popular-names.txt | sed 's/\t/ /g' | cut -f 2 -d " " > col2.txt
