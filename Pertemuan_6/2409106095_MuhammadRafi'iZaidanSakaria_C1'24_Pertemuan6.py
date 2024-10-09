# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])
# print(daftar_buku)

# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku1" : "Twillight"     #key nya gk boleh sama 
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Twillight",
# "Buku3" : "Twillight"    #boleh sama
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#     }
# }

# print(Biodata["KRS"][0:])

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "Izanami#6848"
#     }
# }

# print(Biodata["Social Media"]["Discord"])

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "Izanami#6848",
#         "Email" : "iniemail@gmail.com"
#     }
# }

# print(Biodata["KRS"][0])
# print(Biodata["Social Media"]["Email"])

# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = "FPS")
# print(games["Valorant"])

# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = {"nama" : {"dimas"}})
# print(games['Valorant']['nama'])
# Games = {
#     "Game1" : "PUBG Mobile",
#     "Game2" : "Mobile Legend",
#     "Game3" : "COC"
# }
# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = {"nama" : {123 : "informatika"}} )
# print(games['Valorant']['nama'][123])

# Games = {
#     "Game1" : "PUBG Mobile",
#     "Game2" : "Mobile Legend",
#     "Game3" : "COC"
# }
# print(Games.get('Game3'))

# Games = {
#     "Game1" : "PUBG Mobile",
#     "Game2" : "Mobile Legend",
#     "Game3" : {
#         "nama" : "COC",
#         "genre" : "Strategy"
#     }
# }
# print((Games.get('Game3')).get('genre'))

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }
# #tanpa menggunakan items
# for i in Nilai :
#     print(i)
# print("")

# #menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"}) #bisa di tambahkan sampai banyak tapi pake koma
# #Setelah Ditambah
# print(Film)

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"}) #bisa di tambahkan sampai banyak tapi pake koma
# #Setelah Ditambah
# del Film['Avenger Endgame']
# print(Film)


# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"}) #bisa di tambahkan sampai banyak tapi pake koma
# #Setelah Ditambah
# # del Film['Avenger Endgame']
# # print(Film)

# simpan = Film.pop ('Hours')
# print(Film)
# print(simpan)

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"}) #bisa di tambahkan sampai banyak tapi pake koma
# #Setelah Ditambah
# # del Film['Avenger Endgame']
# # print(Film)

# simpan = Film.pop ('Hours')
# Film.clear()
# print(Film)
# print(simpan)

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"}) #bisa di tambahkan sampai banyak tapi pake koma
# #Setelah Ditambah
# # del Film['Avenger Endgame']
# # print(Film)
# # print(Film)
# # simpan = Film.pop ('Hours')
# # # Film.clear()
# # print(Film)
# # Film["Hours"] = simpan
# # print(Film)
# print("Jumlah Film = ", len(Film))

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"}) #bisa di tambahkan sampai banyak tapi pake koma
# #Setelah Ditambah
# # del Film['Avenger Endgame']
# # print(Film)
# # print(Film)
# # simpan = Film.pop ('Hours')
# # # Film.clear()
# # print(Film)
# # Film["Hours"] = simpan
# # print(Film)
# movies = 
# print("Jumlah Film = ", len(Film))

# key = "apel", "jeruk", "mangga", "semangka"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
#     print(i)
    # print("")
#menggunakan value
# for i in Nilai.values():
#     print(i)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
# print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
# print("")

