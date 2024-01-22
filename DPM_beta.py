import datetime
import os
import string
import random

data = {
    'nama':'nama',
    'nim':'nim',
    'sem':0,
    'lahir':datetime.datetime(1111,1,1)
}

#key = random memilih string asci 6x |bikin 6 random string
data_mahasiswa = {}

os.system("cls")
while True :
    print("="*60)
    print(f"{'DATA MAHASISWA':^60}")
    print("="*60)

    mahasiswa=dict.fromkeys(data.keys())
    mahasiswa['nama']=input("Nama    \t: ")
    mahasiswa['nim']=input("NIM      \t: ")
    mahasiswa['sem']=input("Semester \t: ")
    hari = int(input("Tanggal \t: "))
    bulan = int(input("Bulan \t: "))
    tahun = int(input("Tahun \t: "))
    mahasiswa['lahir']= datetime.datetime(tahun,bulan,hari)
    
    KEY = ''.join(random.choice(string.digits) for i in range(6))
    data_mahasiswa.update({KEY:mahasiswa})

    print("="*60)
    print(f"{'id':<6} {'|Nama':<17} {'|NIM':<10} {'|Semester':<10} {'|Lahir':<10}")
    print('='*60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SEM = data_mahasiswa[KEY]['sem']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')
        print(f"{KEY:<6} |{NAMA:<17}|{NIM:<10}|{SEM:<10}|{LAHIR:<10}")

    print('\n')
    done = input("selesai? (y/n)")
    if done == "y":
        break

print("\nTERIMAKASIH")