import requests
import json

API_KEY = "12ReKcABuIhvdekriuJCz4FBXcU0mX7L"  # Ganti dengan API key kamu
LOCATION_KEY = "203001"  # Kedungtuban, Blora
BASE_URL = "http://dataservice.accuweather.com"

def ambil_prakiraan():
    try:
        # Ambil data cuaca hari ini
        url_today = f"{BASE_URL}/forecasts/v1/daily/1day/{LOCATION_KEY}?apikey={API_KEY}&language=id&metric=true"
        res_today = requests.get(url_today)
        res_today.raise_for_status()
        data_today = res_today.json()
        hari_ini = data_today['DailyForecasts'][0]
        cuaca1 = hari_ini['Day']['IconPhrase']
        suhu_max1 = int(hari_ini['Temperature']['Maximum']['Value'])

        # Ambil data cuaca besok
        url_5day = f"{BASE_URL}/forecasts/v1/daily/5day/{LOCATION_KEY}?apikey={API_KEY}&language=id&metric=true"
        res_5day = requests.get(url_5day)
        res_5day.raise_for_status()
        data_5day = res_5day.json()
        hari_besok = data_5day['DailyForecasts'][1]
        cuaca2 = hari_besok['Day']['IconPhrase']
        suhu_max2 = int(hari_besok['Temperature']['Maximum']['Value'])

        # Format sebagai JSON
        data = {
            "hari_ini": {
                "cuaca": cuaca1,
                "suhu": suhu_max1
            },
            "besok": {
                "cuaca": cuaca2,
                "suhu": suhu_max2
            }
        }

        # Simpan sebagai file JSON
        with open("cuaca.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print("✅ cuaca.json berhasil diperbarui.")
        return True

    except Exception as e:
        print("❌ Gagal ambil cuaca:", e)
        return False

if __name__ == "__main__":
    ambil_prakiraan()
