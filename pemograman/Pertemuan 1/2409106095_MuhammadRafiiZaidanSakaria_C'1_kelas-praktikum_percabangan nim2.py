nim = int(input("Masukan nim : "))
hasil = "kelas A" if nim >= 0 and nim <= 50 else "Kelas B" if nim >= 51 and nim <= 100 else "Kelas C" if nim >= 101 and nim <= 121 else "mahasiswa siluman"
print(hasil)