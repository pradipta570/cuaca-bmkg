import requests

# Ganti dengan kode wilayah adm4 yang benar untuk Kedungtuban, Blora
kode_wilayah = "33.16.04.2016"

url = f"https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4={kode_wilayah}"

def fetch_cuaca_bmkg_api():
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Contoh print data cuaca (sesuaikan dengan struktur JSON yang diterima)
        print("Data cuaca dari API BMKG:")
        print(data)

        # Misal ambil prakiraan hari ini dan besok
        prakiraan = data.get("data", {}).get("prakiraan", [])
        for hari in prakiraan[:2]:
            tanggal = hari.get("tanggal")
            cuaca = hari.get("cuaca")
            suhu_min = hari.get("suhu_min")
            suhu_max = hari.get("suhu_max")
            print(f"{tanggal}: Cuaca {cuaca}, suhu {suhu_min}°C - {suhu_max}°C")

    except Exception as e:
        print("Gagal ambil data dari API BMKG:", e)

if __name__ == "__main__":
    fetch_cuaca_bmkg_api()
