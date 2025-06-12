import requests
import json

API_KEY = "12ReKcABuIhvdekriuJCz4FBXcU0mX7L"  # Ganti dengan API key kamu
LOCATION_KEY = "203001"  # Blora
BASE_URL = "http://dataservice.accuweather.com"

def ambil_prakiraan():
    try:
        # Ambil suhu saat ini
        url_current = f"{BASE_URL}/currentconditions/v1/{LOCATION_KEY}?apikey={API_KEY}&language=id&metric=true"
        res_current = requests.get(url_current)
        res_current.raise_for_status()
        data_current = res_current.json()
        suhu_now = int(data_current[0]['Temperature']['Metric']['Value'])
        cuaca_now = data_current[0]['WeatherText']

        # Ambil cuaca besok (dari 5-day forecast)
        url_5day = f"{BASE_URL}/forecasts/v1/daily/5day/{LOCATION_KEY}?apikey={API_KEY}&language=id&metric=true"
        res_5day = requests.get(url_5day)
        res_5day.raise_for_status()
        data_5day = res_5day.json()
        hari_besok = data_5day['DailyForecasts'][1]
        cuaca2 = hari_besok['Day']['IconPhrase']
        suhu_max2 = int(hari_besok['Temperature']['Maximum']['Value'])

        # Format JSON hasil
        data = {
            "hari_ini": {
                "cuaca": cuaca_now,
                "suhu": suhu_now  # pakai suhu real-time
            },
            "besok": {
                "cuaca": cuaca2,
                "suhu": suhu_max2
            }
        }

        # Simpan ke file JSON
        with open("cuaca.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print("✅ cuaca.json berhasil diperbarui.")
        return True

    except Exception as e:
        print("❌ Gagal ambil cuaca:", e)
        return False

if __name__ == "__main__":
    ambil_prakiraan()
