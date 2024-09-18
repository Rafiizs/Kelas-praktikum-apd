umur = int(input("masukan umur anda : "))
if umur > 0:
    if umur <= 10:
        print("umur anda termasuk kategori anak-anak")
    elif umur <= 18:
        print("umur anda termasuk kategori remaja")
    elif umur <= 35:
        print("umur anda termasuk kategori dewasa")
    elif umur <= 65:
        print("umur anda termasuk kategori paru baya")
    else:
        print("umur anda termasuk ")
    