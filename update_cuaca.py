import requests
import json
from datetime import datetime

API_KEY = "12ReKcABuIhvdekriuJCz4FBXcU0mX7L"  # Ganti sesuai punyamu
LOCATION_KEY = "203001"  # Kedungtuban, Blora
BASE_URL = "http://dataservice.accuweather.com"

def ambil_prakiraan():
    try:
        # Hari ini
        url_today = f"{BASE_URL}/forecasts/v1/daily/1day/{LOCATION_KEY}?apikey={API_KEY}&language=id&metric=true"
        data_today = requests.get(url_today).json()
        hari_ini = data_today['DailyForecasts'][0]
        cuaca1 = hari_ini['Day']['IconPhrase']
        suhu_max1 = int(hari_ini['Temperature']['Maximum']['Value'])

        # Besok
        url_5day = f"{BASE_URL}/forecasts/v1/daily/5day/{LOCATION_KEY}?apikey={API_KEY}&language=id&metric=true"
        data_5day = requests.get(url_5day).json()
        hari_besok = data_5day['DailyForecasts'][1]
        cuaca2 = hari_besok['Day']['IconPhrase']
        suhu_max2 = int(hari_besok['Temperature']['Maximum']['Value'])

        # Format JSON
        cuaca_json = {
            "hari_ini": {
                "cuaca": cuaca1,
                "suhu": suhu_max1
            },
            "besok": {
                "cuaca": cuaca2,
                "suhu": suhu_max2
            }
        }

        with open("cuaca.json", "w", encoding="utf-8") as f:
            json.dump(cuaca_json, f, ensure_ascii=False)

        print("✅ cuaca.json berhasil diperbarui.")
        return True

    except Exception as e:
        print("❌ Gagal ambil cuaca:", e)
        return False

if __name__ == "__main__":
    ambil_prakiraan()
