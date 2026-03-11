'''
Soal 1. Menampilkan Daftar Film
Topik: For Loop, If-Else | Estimasi waktu: 15 menit
Deskripsi:

Buatlah program untuk menampilkan daftar film yang tersedia dan meminta pelanggan
memilih satu film.
Ketentuan Program:

1. Buat list film berisi 5 item film beserta harga tiketnya, contoh: [[ "Danur", 50000 ], [
"Inside Out 2", 45000 ], ...].
2. Tampilkan seluruh daftar film beserta harga menggunakan for loop dengan penomoran.
3. Minta pengguna memasukkan nomor film yang dipilih.
4. Gunakan if-else untuk memvalidasi input: jika nomor tidak valid, tampilkan pesan error;
jika valid, tampilkan judul film dan harga tiket film yang dipilih.
'''

item_film = [["Snow White", 35000],
             ["Frozen", 45000],
             ["Moana", 50000],
             ["Spider Man", 45000],
             ["Cinderella", 35000]]

print("=== LIST FILM ===")

nomor = 0
for nama, harga in item_film:
    nomor += 1
    print(f'{nomor}. {nama} | {harga}')

pilih_film = int(input("\nPilih film 1-5: "))

if pilih_film == 1:
    print("Snow White | 35000")
elif pilih_film == 2:
    print("Frozen | 45000")
elif pilih_film == 3:
    print("Moana | 50000")
elif pilih_film == 4:
    print("Spider Man | 45000")
elif pilih_film == 5:
    print("Cinderella | 35000")
else: 
    print("Error")