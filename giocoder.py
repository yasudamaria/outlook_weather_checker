import urllib
import requests

# 指定地域から緯度経度を取得
def get_giocode(address):
    # APIから情報の取得
    query = urllib.parse.quote(address)
    url = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="+query
    response = requests.get(url)

    #緯度経度を取得（天気API利用のために緯度経度は小数点第4位まで）
    latlng = response.json()[0]["geometry"]["coordinates"]
    lng = round(latlng[0], 4)
    lat = round(latlng[1], 4)
    return lat, lng
