sisi1 = int(input("Masukkan panjang sisi 1: "))
sisi2 = int(input("Masukkan panjang sisi 2: "))
sisi3 = int(input("Masukkan panjang sisi 3: "))

if sisi1 + sisi2 <= sisi3 or sisi1 + sisi3 <= sisi2 or sisi2 + sisi3 <= sisi1:
    print("Yahhh....Ketiga sisi tersebut tidak bisa membentuk segitiga")
elif sisi1 == sisi2 and sisi2 == sisi3:
    print("Segitiga sama sisi")
elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
    print("Segitiga sama kaki")
else:
    print("Segitiga sembarang")