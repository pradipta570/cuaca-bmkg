import requests
from datetime import datetime, timedelta

API_KEY = "12ReKcABuIhvdekriuJCz4FBXcU0mX7L"
LOCATION_KEY = "203001"
BASE_URL = "http://dataservice.accuweather.com"

def get_today_weather(api_key, location_key):
    url = f"{BASE_URL}/currentconditions/v1/{location_key}?apikey={api_key}&language=id-ID&details=true"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data:
            kondisi = data[0]["WeatherText"]
            suhu = data[0]["Temperature"]["Metric"]["Value"]
            return f"Hari ini: {kondisi} {suhu}°C"
    except Exception as e:
        print("Gagal ambil cuaca hari ini:", e)
    return "Hari ini: N/A"

def get_tomorrow_forecast(api_key, location_key):
    url = f"{BASE_URL}/forecasts/v1/daily/5day/{location_key}?apikey={api_key}&language=id-ID&metric=true"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "DailyForecasts" in data and len(data["DailyForecasts"]) >= 2:
            besok = data["DailyForecasts"][1]
            kondisi = besok["Day"]["IconPhrase"]
            suhu = besok["Temperature"]["Maximum"]["Value"]
            return f"Besok: {kondisi} {suhu}°C"
    except Exception as e:
        print("Gagal ambil prakiraan besok:", e)
    return "Besok: N/A"

def simpan_ke_file(teks1, teks2):
    try:
        with open("cuaca.txt", "w", encoding="utf-8") as f:
            f.write(teks1 + "\n")
            f.write(teks2 + "\n")
        print("cuaca.txt berhasil diperbarui.")
    except Exception as e:
        print("Gagal simpan file:", e)

if __name__ == "__main__":
    cuaca_hari_ini = get_today_weather(API_KEY, LOCATION_KEY)
    cuaca_besok = get_tomorrow_forecast(API_KEY, LOCATION_KEY)
    simpan_ke_file(cuaca_hari_ini, cuaca_besok)
