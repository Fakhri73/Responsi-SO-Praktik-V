print("="*50)
print("\t\tMANAJEMEN RAM")
print("="*50)

print()

tRam = int(input("Masukkan total ram (Gb)\t\t :"))
tPetaBit = int(input("Masukkan total petabit (Kb)\t :"))
RamOS = int(input("Ram terpakai sistem operasi(Gb)\t :"))
RamP1 = int(input("Ram terpakai program 1 (Gb)\t :"))
RamP2 = int(input("Ram terpakai program 2 (Gb)\t :"))

#. konversi ram
konvRam = tRam*1024

#. rumus kapasitas per petabit
pb = (tRam/tPetaBit)
kPetaBit = (pb*1048576)

#. rumus total ram
RamTerpakai = (RamOS + RamP1 + RamP2)

#. rumus sisa ram
sRam = (tRam - RamTerpakai)

#. blok terpakai
blokTerpakai = konvRam/kPetaBit/(RamTerpakai*2)


print()

print("="*45)
print("\t\t HASIL PERHITUNGAN")
print("="*45)

print()

print("Total Ram \t\t\t :",tRam,"Gb")
print("Total Petabit \t\t\t :",tPetaBit,"Kb")
print("Kapasitas per petabit \t\t :",kPetaBit,"Kb per blok")
print("Total Ram yang terpakai \t :",RamTerpakai,"Gb")
print("Total Ram yang tidak terpakai\t :",sRam,"Gb")
print("Jumalah blok bernilai 1 \t :",blokTerpakai)
print("jumlah blok bernilai 0 \t\t :",tPetaBit - blokTerpakai)