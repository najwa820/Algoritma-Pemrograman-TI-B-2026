'''
Match dugunakan untuk memilih kode blok mana yang akan dijalankan.
'''
# Match statement
hari = 5
match hari:
    case 1:
        print ("Senin")
    case 2:
        print ("Selasa")
    case 3:
        print ("Rabu")
    case 4:
        print ("Kamis")
    case 5:
        print ("Jumat")
    case 6:
        print ("Sabtu")
    case 7:
        print ("Minggu")

# Default Value
'''
case_ digunakan sebagai default (jika tidak ada case yang cocok)
'''
hari = 5
match hari:
    case 6:
        print ("Sabtu")
    case 7:
        print ("Minggu")
    case _:
        print ("Bukan hari libur")

menu = "Ayam Geprek"
match menu:
    case "Ayam Geprek":
        print ("Harga 15.000")
    case "Ayam Penyet":
        print ("Harga 12.000")
    case _:
        print ("Menu tidak tersedia")
        
# Combine values
'''
| digunakan untuk menggabungkan beberapa nilai yang menghasilkan output yang sama.
'''
hari = 7
match hari:
    case 1 | 2 | 3 | 4 | 5 :
        print ("Bukan hari libur")
    case 6 | 7:
        print ("Hari libur")

# If statements as guards
'''
Guard (if) digunakan untuk pengecekan tambahan selain nilai case
'''
bulan = 5
hari = 4
match hari:
    case 1 | 2 | 3 | 4 | 5 if bulan == 4:
        print ("Hari libur di bulan April")
    case 1 | 2 | 3 | 4 | 5 if bulan == 5:
        print ("Hari libur di bulan Mei")
    case _:
        pass