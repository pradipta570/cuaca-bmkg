import requests
import os

kode_wilayah = "33.16.04.2016"
url = f"https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4={kode_wilayah}"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Authorization": f"Bearer {os.environ.get('BMKG_API_KEY')}"
}

def fetch_cuaca():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        forecast = data.get("data", {}).get("forecast", [])
        if not forecast:
            print("Data forecast kosong")
            with open("cuaca.txt", "w", encoding="utf-8") as f:
                f.write("Tidak ada data cuaca tersedia.")
            return False

        # Process forecast data
        today = datetime.now().date()
        besok = today + timedelta(days=1)
        target_tanggal = {str(today), str(besok)}

        hasil = []
        for item in forecast:
            waktu_str = item.get("local_datetime", "")
            if not waktu_str:
                continue

            tanggal = waktu_str.split(" ")[0]
            if tanggal in target_tanggal:
                waktu = waktu_str
                suhu = item.get("t", "N/A")
                kelembapan = item.get("hu", "N/A")
                cuaca = item.get("weather_desc", "N/A")
                hasil.append(f"{waktu}: {cuaca}, suhu {suhu}°C, kelembapan {kelembapan}%")

        if not hasil:
            print("Tidak ada data cuaca untuk hari ini dan besok.")
            with open("cuaca.txt", "w", encoding="utf-8") as f:
                f.write("Data cuaca untuk hari ini dan besok tidak tersedia.")
            return False

        with open("cuaca.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(hasil))

        print("File cuaca.txt berhasil dibuat.")
        return True

    except Exception as e:
        print(f"Gagal ambil cuaca: {e}")
        with open("cuaca.txt", "w", encoding="utf-8") as f:
            f.write("Gagal mengambil data cuaca: " + str(e))
        return False
