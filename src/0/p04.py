# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭の2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

import re

str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."


def to_elemnt_symbol(itr) -> str:
    idx = itr[0]
    if (idx in [1, 5, 6, 7, 8, 9, 15, 16, 19]):
        return itr[1][0], idx
    else:
        return itr[1][0:2], idx


itr1 = filter(lambda x: len(x) > 0, re.split(r'[\s,\.]+', str1))
itr2 = map(to_elemnt_symbol, enumerate(itr1, 1))

print(dict(itr2))
