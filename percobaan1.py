# fungsi menghitung gaji
def hitungGaji(nama, nik, status, golongan):

    # data (dari soal)
    gaji_tetap = {"A": 200000, "B": 400000, "C": 550000}
    gaji_honor = {"A": 150000, "B": 275000, "C": 480000}

    # penentuan gaji dari status dan golongan
    if status.lower() == "tetap":
        gaji = 1000000
        bonus = gaji_tetap.get(golongan.upper(), 0)
    elif status.lower() == "honor":
        gaji = 750000
        bonus = gaji_honor.get(golongan.upper(), 0)
    else:
        print("Status tidak valid!")
        return

    # total gaji
    gaji_total = gaji + bonus

    # display
    print("\n=== Slip Gaji ===")
    print("Nama      : " + nama)
    print("NIK       : " + nik)
    print("Status    : " + status)
    print("Golongan  : " + golongan)
    print("Gaji      : Rp", gaji)
    print("Bonus     : Rp", bonus)
    print("Gaji Total: Rp", gaji_total)

# input user
nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Pegawai Tetap/Honor): ")
golongan = input("Masukkan Golongan (A/B/C): ")

# panggil fungsi hitung_gaji
hitungGaji(nama, nik, status, golongan)