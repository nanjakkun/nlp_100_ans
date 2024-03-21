# テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
# https://www.mediawiki.org/wiki/API:Imageinfo

import json
import urllib.parse
import urllib.request

file_name = "Flag of the United Kingdom.svg"
url = 'https://www.mediawiki.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url&titles=File:' + \
    urllib.parse.quote(file_name)

response = json.loads(urllib.request.urlopen(
    urllib.request.Request(url)).read().decode())

print(response['query']['pages']['-1']['imageinfo'][0]['url'])
