print("="*50)
print("\tMANAJEMEN PENJADWALAN ROUND ROBIN")
print("="*50)

proses = []
bTime = [] #. Digunakan menyimpan sisa waktu

nProses = int(input("Masukkan Banyak Program \t :"))
print("Masukkan nomor program dan lama prosesnya")

for _ in range (nProses) :
    proses.append(list(map(int, input(). split())))
    bTime.append(proses[-1][1])

quantum = int(input("Masukkan Jatah Waktu \t\t :"))
tbTime = sum(bTime)

ct=0
i = 0
while(tbTime>ct):
    if(bTime[i]>quantum):
        bTime[i] -= quantum
        ct+=quantum
    elif(bTime[i] != 0):
        ct+=bTime[i]
        bTime[i]=0
        proses[i].append(ct)
    i += 1
    i%=nProses

rata_waktu = 0
waktu_tunggu = 0

for i in range(nProses):
    rata_waktu += proses[i][2]
    waktu_tunggu += proses[i][2]-proses[i][1]

print("Waktu penyelesaian \t\t :" , rata_waktu /nProses)
print("Waktu rata- rata tunggu \t :", waktu_tunggu /nProses)
