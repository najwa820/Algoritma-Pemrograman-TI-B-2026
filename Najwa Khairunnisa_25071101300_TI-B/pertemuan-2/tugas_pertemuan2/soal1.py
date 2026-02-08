'''
Buat sebuah fungsi bernama rata rata(nilai) yang:
1. Menerima sebuah list berisi nilai mahasiswa
2. Menghitung rata-rata nilai
3. Jika list kosong, kembalikan pesan: "Data kosong"
Kemudian:
1. Panggil fungsi dengan list: [80, 75, 90, 60, 85]
2. Tampilkan hasilnya
'''

def rata_rata(nilai):
    if nilai == []:
        print ("Data Kosong")
        return 
    
    total = 0
    jumlah = 0

    for x in nilai:
        jumlah += x
        total += 1
    return jumlah / total

print(rata_rata ([80, 75, 90, 60, 85]))