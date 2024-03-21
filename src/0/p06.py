# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．

# 前回の問題で使ったのと同じ関数
def char_n_gram(text, num=2):
    words = text.replace(" ", "")
    return list(map(lambda i: words[i:i+num], range(len(words))))


text1 = "paraparaparadise"
text2 = "paragraph"

X = set(char_n_gram(text1))
Y = set(char_n_gram(text2))

print("union: ", X | Y)
print("intersect: ", X & Y)
print("diff: ", X - Y)

if "se" in X:
    print("X contains se")

if "se" in Y:
    print("Y contains se")
