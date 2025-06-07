import requests

API_KEY = "12ReKcABuIhvdekriuJCz4FBXcU0mX7L"  # ganti dengan API key kamu
LOCATION_NAME = "Kedungtuban"

def get_location_key(location_name):
    url = f"https://dataservice.accuweather.com/locations/v1/cities/search"
    params = {
        "apikey": API_KEY,
        "q": location_name
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    locations = response.json()
    if locations:
        return locations[0]["Key"]
    else:
        raise Exception("Lokasi tidak ditemukan")

def get_current_weather(location_key):
    url = f"https://dataservice.accuweather.com/currentconditions/v1/{location_key}"
    params = {
        "apikey": API_KEY,
        "language": "id-ID",
        "details": "true"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    weather_data = response.json()
    if weather_data:
        return weather_data[0]
    else:
        raise Exception("Data cuaca tidak tersedia")

def save_weather_to_file(weather):
    with open("cuaca.txt", "w", encoding="utf-8") as f:
        f.write(f"Tanggal & Waktu: {weather['LocalObservationDateTime']}\n")
        f.write(f"Cuaca: {weather['WeatherText']}\n")
        f.write(f"Suhu: {weather['Temperature']['Metric']['Value']} °C\n")
        f.write(f"Kelembapan: {weather['RelativeHumidity']} %\n")
        f.write(f"Kecepatan Angin: {weather['Wind']['Speed']['Metric']['Value']} km/jam\n")

def main():
    try:
        location_key = get_location_key(LOCATION_NAME)
        weather = get_current_weather(location_key)
        save_weather_to_file(weather)
        print("Data cuaca berhasil disimpan ke cuaca.txt")
    except Exception as e:
        print("Gagal mengambil data cuaca:", e)

if __name__ == "__main__":
    main()
