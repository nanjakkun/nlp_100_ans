# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．

def word_n_gram(text, num=2):
  words = text.split(" ")
  return list(map(lambda i: words[i:i+num], range(len(words))))

def char_n_gram(text, num=2):
  words = text.replace(" ", "")
  return list(map(lambda i: words[i:i+num], range(len(words))))

text1 = "I am an NLPer"

print(word_n_gram(text1, 2))
print(char_n_gram(text1, 2))
