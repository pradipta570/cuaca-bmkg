import requests
import datetime

# URL file JSON cuaca resmi BMKG untuk Kab. Blora
URL = "https://raw.githubusercontent.com/infoBMKG/data-cuaca/main/cuaca/kab-blora.json"

def fetch_cuaca():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        with open("cuaca.txt", "w", encoding="utf-8") as f:
            f.write("Gagal ambil cuaca")
        print("Gagal ambil cuaca:", e)
        return

    hasil = []

    tanggal = data.get("tanggal", "")
    kota = data.get("kota", "Blora")
    entries = data.get("data", [])

    if not entries:
        hasil.append("Data kosong")
    else:
        hasil.append(f"{kota} {tanggal}")
        for entry in entries:
            jam = entry.get("jam", "-")
            cuaca = entry.get("cuaca", "-")
            suhu = entry.get("suhu", "-")
            hasil.append(f"{jam} {cuaca} {suhu}C")

    # Simpan ke cuaca.txt
    with open("cuaca.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(hasil))
    print("Berhasil update cuaca.txt")

if __name__ == "__main__":
    fetch_cuaca()
