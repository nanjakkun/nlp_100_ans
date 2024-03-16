# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，
# その実行結果を確認せよ．

import random

def typoglycemia(text) -> str:
  def shuffle(word) -> str:
    if (len(word) <= 4):
      return word
    else:
      substr = word[1:-1:]
      return word[0] + "".join(random.sample(substr, len(substr))) + word[-1]

  words = text.split(" ")
  return " ".join(map(shuffle, words))

text1 = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(text1))
