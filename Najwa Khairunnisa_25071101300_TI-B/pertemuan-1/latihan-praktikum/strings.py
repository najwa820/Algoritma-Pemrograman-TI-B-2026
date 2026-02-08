'''
Di Python penulisan string bisa menggunakan "" atau ''
'''

print ("Aku mau pergi")
print ("Aku bertemu teman lamaku, namanya 'Inayah'")    # Aku bertemu teman lamaku, namanya 'Inayah'
print ('Aku bertemu teman lamaku, namanya "Inayah"')    # Aku bertemu teman lamaku, namanya "Inayah"

# Multiline Strings
a = '''Pergi pagi ke tepi pantai,
Angin sepoi menemani perjalanan,
Liburan datang hati berseri,
Penat hilang berganti kesenangan.
'''
print (a)

# Strings are Arrays
'''
Di Python, string bisa dianggap sebagai Array
'''
a = "Mie Ayam!"
print (a[2], a[3], a[4], a[8])      # Outputnya "e", " ", "A", "!"
print (a[2:5])                      # Outputnya "e A" (dimulai dari indeks ke 2 sampai 4)
print (a[:3])                       # Outputnya "Mie" (dimulai dari indeks ke 0 sampai 2)
print (a[1:])                       # Outputnya "ie Ayam!" (dimulai dari indeks ke 1 sampai 8)
print (a[-4:-1])                    # Outputnya "yam" (perhitungan indeks nya dari belakang yaitu !=-1)

# Looping Trough a String
for x in "bakso bakar":
    print (x)       # Setiap huruf akan dicetak satu per satu ke bawah

# String Length
a = "Mie Ayam!"
print (len(a))      # Outputnya menghitung ada berapa isi di dalam variabel

# Check String
teks = "Kami akan bermain roblox"
print ("roblox" in teks)        # Outputnya akan True karena roblox ada di variabel
print ("mountain" in teks)      # Outputnya akan False karena mountain tidak ada di variabel

if "roblox" in teks:
    print ("Kami bermain roblox")   # Akan dijalankan jika kondisi bernilai True

# Check if NOT
teks = "Kami akan bermain roblox"
print ("roblox" not in teks)    # Outputnya akan False karena roblox ada didalam variabel
print ("mountain" not in teks)  # Outputnya akan True karena mountai tidak ada didalam variabel

if "mountain" not in teks:      
    print ("Kami akan mendaki") 

# Upper Case
'''
Mengubah menjadi huruf kapital
'''
a = "Mie Ayam!"
print (a.upper())               # Outputnya "MIE AYAM!"

# Lower Case
'''
Mengubah menjadi huruf kapitil
'''
a = "Mie Ayam!"
print (a.lower())               # Outputnya "mie ayam!"

# Remove Whitespace
'''
Menghapus spasi 
'''
a = " Mie Ayam! "
print (a)                       # Jika tidak menggunakan strip outputnya akan terbaca spasi yang dibuat " Mie Ayam!"
print (a.strip())               # Outputnya "Mie Ayam!" (spasi nya dihapus)

# Replace String
'''
Menukar huruf
'''
a = "Mie Ayam!"
print (a.replace("M", "A"))     # Mengubah huruf "M" menjadi huruf "A"

# Split String
'''
split() digunakan untuk meemcah string menjadi list 
'''
x = "Aku-suka-belajar"
print (x.split("-"))            # Outputnya ["Aku", "suka", "belajar"]

# String Concatenation
'''
Untuk menggabungkan dua string menggunakan operator +
'''
a = "Hobiku"
b = "Bersepeda"
print (a + b)                    # Outputnya "HobikuBersepeda"
print (a + " " + b)              # Outputnya "Hobiku Bersepeda"

# Format String
angka = 18
print (f'aku berumur {angka} tahun')
print (f'ibu membeli {angka:.2f} kg apel')
print (f'total uang adik adalah {3*18} dollar')

# Escape Characters\
'''
Escape Characters digunakan untuk menuliskan karakter khusus di dlaam string yang sebenarnya tidak boleh langsung ditulis
'''
#1 \' -> Single Quote
print ('Aku bertemu teman bernama \'inayah\'')      # Outputnya Aku bertemu teman bernama 'Inayah'
#2 \" -> Double Quote
print ("Dia berkata \"Aku suka belajar\"")          # Outputnya Dia berkata "Aku suka belajar"
#3 \\ -> Backslash
print ("Alamat file: C:\\Users\\Najwa")             # Outputnya Alamat file: C:\Users\Najwa
#4 \n -> New Line (baris baru)
print ("Halo\nSemua")                               # Outputnya kata Semua akan di letakkan di baris baru
#5 \t -> Tab
print ("Nama:\tNajwa")                              # Outputnya Nama:   Najwa
#6 \r -> Carriage Return
print ("Hallo\rHai")                                # Outputnya Hai (Hallo ditimpa dengan Hai)
#7 \b -> Backspace
print ("Halloo\b")                                  # Outputnya Hallo (satu huruf terakhir o dihapus)
#8 \f -> form Feed
print ("Hallo\fWorld")                              # Outputnya Hallo World (ada spasi nya)
#9 \ooo -> Nilai Oktal
print ("\101")                                      # Outputnya A karena 101 (oktal) jika dikonversi hasilnya 65, dalam tabel ASCII 65 adalah huruf A
#10 \xhh -> Nilai Hexadecimal
print ("\x41")                                      # Outputnya A karena 41 (hex) jika dikonversi hasilnya 65, dalam tabel ASCII 65 adalah huruf A

# String Method
#1 capitalize() -> Huruf pertama jadi besar
teks = "hallo world"
print (teks.capitalize())                           # Outputnya Hallo world
#2 title() -> Huruf pertama tiap kata jadi besar
print (teks.title())                                # Outputnya Hallo World
#3 swapcase -> besar <-> kecil
print (teks.swapcase())                             # Outputnya HALLO WORLD