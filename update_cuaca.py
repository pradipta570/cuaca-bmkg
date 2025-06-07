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

        prakiraan = data.get("data", {}).get("prakiraan", [])
        if not prakiraan:
            print("Data prakiraan kosong")
            return False

        with open("cuaca.txt", "w", encoding="utf-8") as f:
            for hari in prakiraan[:2]:  # hari ini dan besok
                tanggal = hari.get("tanggal", "N/A")
                cuaca = hari.get("cuaca", "N/A")
                suhu_min = hari.get("suhu_min", "N/A")
                suhu_max = hari.get("suhu_max", "N/A")
                f.write(f"{tanggal}: {cuaca}, suhu {suhu_min} - {suhu_max} °C\n")
        print("File cuaca.txt berhasil dibuat.")
        return True

    except Exception as e:
        print("Gagal ambil cuaca:", e)
        if 'response' in locals():
            print("Status:", response.status_code)
            print("Response:", response.text[:500])
        return False

if __name__ == "__main__":
    fetch_cuaca()
