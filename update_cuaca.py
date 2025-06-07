import requests

API_KEY = "12ReKcABuIhvdekriuJCz4FBXcU0mX7L"
LOCATION_KEY = "203001"
BASE_URL = "http://dataservice.accuweather.com"

def get_current_weather(api_key, location_key):
    url = f"{BASE_URL}/currentconditions/v1/{location_key}?apikey={api_key}&language=id-ID&details=true"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if not data:
            print("Data cuaca kosong")
            return None

        kondisi = data[0]["WeatherText"]
        suhu = data[0]["Temperature"]["Metric"]["Value"]
        suhu_unit = data[0]["Temperature"]["Metric"]["Unit"]

        hasil = f"Hari ini: {kondisi}, suhu {suhu}°{suhu_unit}"
        return hasil
    except Exception as e:
        print("Gagal ambil cuaca:", e)
        return None

def simpan_ke_file(teks):
    try:
        with open("cuaca.txt", "w", encoding="utf-8") as f:
            f.write(teks + "\n")
        print("cuaca.txt berhasil dibuat.")
    except Exception as e:
        print("Gagal simpan file:", e)

if __name__ == "__main__":
    cuaca = get_current_weather(API_KEY, LOCATION_KEY)
    if cuaca:
        simpan_ke_file(cuaca)
