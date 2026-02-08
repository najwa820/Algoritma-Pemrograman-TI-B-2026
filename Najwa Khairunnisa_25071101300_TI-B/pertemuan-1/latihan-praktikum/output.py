'''
Output adalah hasil yang ditampilkan setelah dijalankan.
Output yang ditampilkan menggunakan fungsi print().
'''
#1) Menggunakan variabel
nama = "Najwa"
print ("Nama saya", nama)       # Menggunakan "" dan menggunakan , untuk memisahkan string dan variabel
print ('Nama saya', nama)       # Menggunakan '' dan menggunakan , untuk memisahkan string dan variabel
print ("Nama saya " + nama)     # Menggabungkan string dan variabel menggunakan +,  note: variabelnya harus bertipe string
print (f'Nama saya {nama}')     # Menggunakan f-string

#2) Menampilkan Text
print ("Aku lagi belajar")      # Menggunakan ""
print ('Aku lagi belajar')      # Menggunakan ''
print ('Aku lagi belajar "Kalkulus dan Pemrograman"')       # Menggunakan '' untuk menampilkan ""

print ("Halo semuanya", end= " ")   # end= " " digunakan agar output tidak berpindah ke baris baru
print ('Nama saya Najwa')

#3) Menampilkan Numbers
print (25032007)
print (3 + 7)       # Operasi penjumlahan
print (2 - 1)       # Operasi pengurangan
print (3 * 5)       # Operasi perkalian
print (10 / 2)      # Operasi pembagian

#4) Menampilkan Text dan Number dalam satu baris
print ("Sekarang tanggal", 25, "bulan januari", 2026)

#5) Perbedaan menulis number menggunakan "" dan tidak menggunakan ""
# Angka yang ditulis menggunakan "" akan dianggap sebagai string
print (10 + 5)          # Output nya akan 15 (hasilnya dijumlahkan)
print ("10" + "5")      # Output nya akan 105 (hasilnya digabungkan)