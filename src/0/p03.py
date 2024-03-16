# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

import re

str1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
itr1 = map(lambda str: len(str), re.split(r'[\s,\.]+', str1))
itr2 = filter(lambda x: x > 0, itr1)
print(list(itr2))
