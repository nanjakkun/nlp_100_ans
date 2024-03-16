# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# - 英小文字ならば(219 - 文字コード)の文字に置換
# - その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(text: str) -> str:
  def transform_char(ch):
    if (97 < ord(ch) & ord(ch) < 122):
      return chr(219 - ord(ch))
    else:
      return ch

  return "".join(list(map(transform_char, text)))

text1 = "lorem ipsum"
print(cipher(text1))
print(cipher(cipher(text1)))
