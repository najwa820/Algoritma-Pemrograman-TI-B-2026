'''
Soal 2. Menghitung Total Pembelian Tiket
Topik: While Loop, For Loop | Estimasi waktu: 20 menit
Deskripsi:

Berdasarkan Soal 1 kembangan kode agar pelanggan dapat membeli tiket untuk lebih dari
satu film (atau lebih dari satu jenis tiket) dan program menghitung total harga seluruh
pembelian.

Ketentuan Program:
1. Gunakan while loop agar pelanggan dapat terus menambah pembelian tiket. Loop berhenti
ketika pelanggan memasukkan angka 0.
2. Simpan setiap pembelian ke dalam sebuah list berisi judul film dan jumlah tiket.
3. Setelah selesai, tampilkan daftar pembelian menggunakan for loop beserta subtotal tiap
item (harga tiket x jumlah tiket).
4. Tampilkan total harga keseluruhan di bagian akhir.
'''

item_film = [["Snow White", 35000],
             ["Frozen", 45000],
             ["Moana", 50000],
             ["Spider Man", 45000],
             ["Cinderella", 35000]]

nomor = 0
for nama, harga in item_film:
    nomor += 1
    print(f'{nomor}. {nama} | {harga}')

pembelian_tiket = 0
data = []

y = 1

while y:
    tambah = int(input("1 = Tambah, 0 = Stop: "))
    pembelian_tiket += 1

    if tambah == 0:
        y = 0
    elif 1 <= tambah <= 5:
        print("Tidak Valid")
        
    else:
        print(f'{item_film[harga]}')
        data.append({item_film[harga]})

print (data)

print("=== TAMPILAN ===")
total = harga * pembelian_tiket
print(total)