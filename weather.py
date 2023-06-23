import requests

# Meteo Weather APIから今日の天気コードを取得 
def get_weather(lat, lng):
    url = "https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&longitude=" + str(lng) + "&hourly=weathercode&forecast_days=1&timezone=Asia%2FTokyo"
    weather_today = requests.get(url).json()

    return(weather_today)

# 特定時間の天気こーどを取得
def weather_jedge(lat, lng, hour):
    
    date = get_weather(lat, lng)
    weather_code = date["hourly"]['weathercode'][hour]
    if weather_code > 60:
        return("雨が降るでしょう")
    else:
        return("晴れるでしょう")
