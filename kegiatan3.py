# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(uts, uas):
    return (uts + uas) / 2

# Fungsi untuk menghitung nilai akhir semua mahasiswa
def hitung_nilai_akhir_semua(data_mahasiswa):
    data_nilai_akhir = {}  # Membuat dictionary untuk menyimpan nilai akhir mahasiswa
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

# Fungsi untuk menampilkan nilai akhir mahasiswa
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        'Mahasiswa1': {'uts': 85, 'uas': 78},
        'Mahasiswa2': {'uts': 70, 'uas': 92},
        'Mahasiswa3': {'uts': 92, 'uas': 88},
        # Tambahkan data mahasiswa lainnya di sini
    }

    data_nilai_akhir = hitung_nilai_akhir_semua(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()
