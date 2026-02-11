#soal 1
nilai = [75, 80, 65, 90, 85]

#1
nilai = [75, 80, 65, 90, 85]
nilai.append(95)
print(nilai)

#2
nilai = [75, 80, 65, 90, 85]
nilai.pop(2)
print(nilai)

#3
nilai = [75, 80, 65, 90, 85]
nilai.sort()
print(nilai)

#4
nilai = [75, 80, 65, 90, 85]
print (max(nilai))
print(min(nilai))
print(len(nilai))

#5
nilai = [75, 80, 65, 90, 85, 95]
print (sum(nilai) / len(nilai))

#6
print (nilai)




#soal 2
dosen = ("D001", "Dr. Andi", "Struktur Data", 12)

#1
dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
print(dosen[1:-1])

#2
dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
for x in dosen:
  print(x)


#3
dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
y = list(dosen)
y[3] = 14
dosen = tuple(y)

print(dosen)

#4
'''
tupple gabisa diubah, sedangkan list bisa diubah
'''

#soal 3
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}

#1
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}

keahlian_AB = keahlian_A.union(keahlian_B)
print(keahlian_AB)

#2
keahlian_Akeahlian_A = frozenset({"Python", "Java", "SQL", "Git"})
print(keahlian_Akeahlian_A)

#3
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}

keahlian_AB = keahlian_A | (keahlian_B)
print(keahlian_AB)


#4
keahlian_B = {"Python", "C++", "Git", "Docker"}

print("Java" in keahlian_B)

#soal 4
mahasiswa = {
"M001": {"nama": "Rina", "prodi": "Informatika", "ipk":
3.60},
"M002": {"nama": "Doni", "prodi": "Sistem Informasi",
"ipk": 3.25},
"M003": {"nama": "Lina", "prodi": "Informatika", "ipk":
3.80}
}
