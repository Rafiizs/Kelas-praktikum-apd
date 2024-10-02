# nama = ["shandy",106,True,3.96]
# matkul =["APD","APL","WEB","JARKOM"]
# print(nama)
# print(matkul)

# nama = ["shandy",106,True,3.96]
# matkul =["APD","APL","WEB","JARKOM"]
# print(nama[1])

# nama = ["shandy",106,True,3.96]
# matkul =["APD","APL","WEB","JARKOM"]
# print(matkul[2])

# nama = ["shandy",106,True,3.96]
# matkul =["APD","APL","WEB","JARKOM"]
# print(matkul[-1])

# nama = ["shandy",106,True,3.96]
# matkul =["APD",
#          "APL",
#          "WEB",
#          "JARKOM",
#          "BASDAT",
#          "STRUKDAT",
#          "PTI",
#          "KALKULUS",
#          "PROBAS"
# ]
# print(matkul[6])

# nama = ["shandy",106,True,3.96,[123,"ALVITO",False,3.66]]
# print(nama[4])

# nama = ["shandy",106,True,3.96,[123,"ALVITO",False,3.66]"Raihan"]
# print(nama[4][2])

# nama = ["shandy",106,True,
#         ["yuyun",145],
#         3.96,
#         [123,"ALVITO",False,3.66],
#         "rehan"
# ]
# print(nama[5][0])

# makanan = ["Bakso","Sate","Soto","nasi goreng","mie ayam",""]
# print("Sebelum: ")
# print(makanan[:2])
# makanan.append("Nasi Goreng")
# print("Sesudah: ")
# makanan.clear()
# print(makanan)
# data = makanan.pop(5)
# print(makanan)
# print(data)
# del makanan[]
# print(makanan)
# makanan.insert(0,"Nasi Goreng")
# makanan[1] = ["AYAM","BEBEK"]
# print(makanan)

# minuman 6. 3(dihapus) 6(air putih) 1(jus tomat)

# minuman = ["es teh","es jeruk","jus alpukat","jus semangka","jus tomat","jus nangka","jus sirsak"]
# print("sebelum: ")
# print(minuman)
# del minuman[2]
# print("sesudah: ")
# print(minuman)
# minuman[4] = "air putih"
# print(minuman)
# minuman.insert(0,"jus tomat")
# print(minuman)

# makanan = ["bakso","soto","sate","ikan","bebek"]

# for i in makanan :
#     print(i)

# makanan = ["bakso","soto","sate","ikan","bebek"]

# for i in makanan :
#     print(i, end=" ")

# makanan = [["bakso","soto","sate","ikan","bebek"],["teh","kopi","air"]]

# for i in makanan :
#     for j in i :
#         print(j, end=" ")

# makanan = ["ayam","ikan",["bakso","soto","sate","ikan","bebek"],["teh","kopi","air"]]

# for i in makanan :
#     if isinstance(1, list):
#         for j in i :
#             print(j)
#     else:
#         print(i)

# akuns = []

# while True:
#     print("Halo Selamat datang di aplikasi Catatan")
#     print("Silahkan pilih 'Daftar Akun' jika belum buat akun, dan jika sesudah memiliki akun silahkan 'login'")
#     print("1. Daftar akun")
#     print("2. Login")
#     print("3. Exit")
#     print("                                        ")
#     opsi = input("pilih opsi: ")
#     print(" ")

#     if opsi == "1":
#         print("Halo baru! ayo buat akun dulu")
#         Username = input("Username: ")
#         akuns = False
#         for akun in akun:
#             if akun[0] == Username: # Memerikasa apakah username sudah ada
#                 akuns = True
#                 break
#         if akuns:
#             print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
#         else:
#             Password = input("Password: ")
#             akuns.append([Username, Password, []]) # Simpan username, Password, dan catatan (sebagai list kosong)
#             print(f"Akun Anda berhasil terdaftar dengan ID: {Username}")