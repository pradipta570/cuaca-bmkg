import requests
from datetime import datetime
import json

API_KEY = "12ReKcABuIhvdekriuJCz4FBXcU0mX7L"  # Ganti dengan API key kamu
LOCATION_KEY = "203001"  # Kedungtuban, Blora
BASE_URL = "http://dataservice.accuweather.com"

def ambil_prakiraan():
    try:
        # Prakiraan 1 hari ke depan (hari ini)
        url_today = f"{BASE_URL}/forecasts/v1/daily/1day/{LOCATION_KEY}?apikey={API_KEY}&language=id&metric=true"
        res_today = requests.get(url_today)
        res_today.raise_for_status()
        data_today = res_today.json()
        hari_ini = data_today['DailyForecasts'][0]
        tanggal1 = datetime.strptime(hari_ini['Date'][:10], "%Y-%m-%d").strftime("%d/%m")
        cuaca1 = hari_ini['Day']['IconPhrase']  # Cuaca hari ini
        suhu_max1 = int(hari_ini['Temperature']['Maximum']['Value'])  # Suhu maksimum hari ini

        # Prakiraan 2 hari ke depan (besok)
        url_5day = f"{BASE_URL}/forecasts/v1/daily/5day/{LOCATION_KEY}?apikey={API_KEY}&language=id&metric=true"
        res_5day = requests.get(url_5day)
        res_5day.raise_for_status()
        data_5day = res_5day.json()
        hari_besok = data_5day['DailyForecasts'][1]
        tanggal2 = datetime.strptime(hari_besok['Date'][:10], "%Y-%m-%d").strftime("%d/%m")
        cuaca2 = hari_besok['Day']['IconPhrase']  # Cuaca besok
        suhu_max2 = int(hari_besok['Temperature']['Maximum']['Value'])  # Suhu maksimum besok

        # Format output dalam JSON
        cuaca_json = {
            "hari_ini": {
                "tanggal": tanggal1,
                "kondisi": cuaca1,
                "suhu_max": suhu_max1
            },
            "besok": {
                "tanggal": tanggal2,
                "kondisi": cuaca2,
                "suhu_max": suhu_max2
            }
        }

        # Simpan data cuaca dalam cuaca.json
        with open("cuaca.json", "w", encoding="utf-8") as json_file:
            json.dump(cuaca_json, json_file, ensure_ascii=False, indent=2)  # Format JSON yang terindetasi untuk keterbacaan

        print("✅ cuaca.json berhasil diperbarui.")
        return True

    except Exception as e:
        print("❌ Gagal ambil cuaca:", e)
        return False

if __name__ == "__main__":
    ambil_prakiraan()
