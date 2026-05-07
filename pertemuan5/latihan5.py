# Latihan 5

#soal 1
stok_barang = [15, 40, 30, 10, 25]

#a
print(stok_barang.index(10))
stok_barang[3] = 50
print(stok_barang)

#b
stok_barang.append(5)
stok_barang.sort(reverse=True)
print(stok_barang)

#c
print(sum(stok_barang))

#d
rata_rata = sum(stok_barang) / len(stok_barang)
status_stok = "Stok Aman" if rata_rata > 20 else "Waspada"
print(status_stok)



#soal 2
data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]

#a
for nama, poin in data_aktivitas:
    if poin > 80:
        print(f"{nama} mendapatkan predikat Gold")
    elif 50 <= poin <= 80:
        print(f"{nama} mendapatkan predikat Silver")
    else:
        print(f"{nama} mendapatkan predikat Bronze")        



#soal 3
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

#a
hanya_coding = ukm_coding - ukm_robotik
print(hanya_coding) 

#b
seluruh_mahasiswa = ukm_coding.union(ukm_robotik)
print(seluruh_mahasiswa)

#c
print (True) if "Andi" in ukm_robotik else print (False)


#soal 4
gudang_pc = [
    {"item": "Monitor", "harga": 1500000, "stok": 5},
    {"item": "Keyboard", "harga": 400000, "stok": 12, "kategori": "Aksesoris"},
    {"item": "Mouse", "harga": 250000, "stok": 20},
    {"item": "Headset", "harga": 350000, "stok": 8}
]

#a
gudang_pc[1]["kategori"] = "Aksesoris"
print(gudang_pc)

#b
gudang_pc.append({"item": "Headset", "harga": 350000, "stok": 8})
print(gudang_pc)

#c
for i in range (len(gudang_pc)):
    total_aset = gudang_pc[i]["harga"] * gudang_pc[i]["stok"]
    print(f"Item: {gudang_pc[i]['item']} | Total Aset: Rp {total_aset}")