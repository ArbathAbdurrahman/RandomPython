absensi = []
while True:
    print("="*40)
    print(f"{'Input Absensi':^40}")
    print("="*40)
    nama = input("Nama\t\t : ")
    keterangan = input("Keterangan\t :")

    data = [nama,keterangan]
    absensi.append(data)

    print("="*40)
    print(f"{'Absensi':^40}")
    print("="*40)
    for index,invut in enumerate(absensi):
        print(f"{index+1} | {invut[0]:^20} | {invut[1]:^15}")
    
