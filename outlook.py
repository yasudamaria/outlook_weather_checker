import win32com.client
import datetime
import giocoder
import weather
# outlookカレンダーのデスクトップアプリから使用者のカレンダー情報を取得
calendar = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI").GetDefaultFolder(9)

#カレンダーから取得した予定
items = calendar.Items

# 指定した期間内の予定を入れるリスト
select_items = []

# 予定を抜き出したい期間を指定
date = datetime.date.today()

# 上記の
#期間の予定リストを作成
for item in items:
    if date == item.start.date():
        select_items.append(item)

# 抜き出した予定の詳細を表示
for select_item in select_items:

    #変数の定義
    address = []
    time = []
    address = str(select_item.location)
    time = int(str(select_item.start)[10:13])

    if address:
        # #緯度経度の取得
        lat= giocoder.get_giocode(address)[0]
        lng = giocoder.get_giocode(address)[1]

        #天気の取得
        weather_output = weather.weather_jedge(lat, lng, time)
        print("-----")
        print(str(time) + "時:"+ select_item.subject+"の時は"+weather_output)
        print("場所：", select_item.location)
        print("-----")
        
    else:
        print("-----")
        print(str(time) + "時:"+ select_item.subject)
        print("場所：", select_item.location)
        print("-----")
        

