import requests
import json
from datetime import datetime

def fetch_cuaca():
    try:
        # URL data cuaca BMKG (contoh JSON wilayah Jawa Tengah)
        url = "https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-Jawa_Tengah.xml"

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Cari kota Kedungtuban di data BMKG
        lokasi = None
        for lokasi_data in data['Forecast']['area']:
            if lokasi_data['name'].lower() == 'kedungtuban':
                lokasi = lokasi_data
                break

        if lokasi is None:
            raise Exception("Lokasi Kedungtuban tidak ditemukan di data BMKG.")

        # Ambil tanggal hari ini dan besok (format YYYY-MM-DD)
        tanggal_hari_ini = datetime.now().strftime('%Y-%m-%d')
        tanggal_besok = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')

        # Fungsi untuk cari parameter cuaca (misal kondisi cuaca) berdasarkan tanggal
        def get_cuaca_per_hari(tanggal):
            for parameter in lokasi['parameter']:
                if parameter['id'] == 'weather':
                    for timerange in parameter['timerange']:
                        # timerange['datetime'] format: YYYYMMDDHHMM, kita ambil tanggalnya saja
                        tgl = timerange['datetime'][:8]
                        if tgl == tanggal.replace('-', ''):
                            return timerange['value'][0]['value']  # kode cuaca
            return "N/A"

        cuaca_hari_ini = get_cuaca_per_hari(tanggal_hari_ini)
        cuaca_besok = get_cuaca_per_hari(tanggal_besok)

        # Format hasil output sederhana
        hasil = (
            f"Kota: Kedungtuban, Blora\n"
            f"Tanggal hari ini: {tanggal_hari_ini}\n"
            f"Cuaca hari ini: {cuaca_hari_ini}\n"
            f"Cuaca besok: {cuaca_besok}\n"
        )

        # Simpan ke file cuaca.txt
        with open('cuaca.txt', 'w', encoding='utf-8') as f:
            f.write(hasil)

        print("Berhasil update cuaca.txt")

    except Exception as e:
        with open('cuaca.txt', 'w', encoding='utf-8') as f:
            f.write(f"Gagal ambil cuaca: {str(e)}")
        print(f"Error: {e}")

if __name__ == "__main__":
    from datetime import timedelta
    fetch_cuaca()
