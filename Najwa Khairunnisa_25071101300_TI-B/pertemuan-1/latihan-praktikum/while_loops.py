'''
Menjalankan statemants selama bernilai True. Jika kondisi False, perulangan akan berhenti.
'''

# The while loop
a = 10          # Nilai awal
while a > 5:    # Perulangan selama a > 5
    print (a)
    a -= 2      # Mengurangi nilai a setiap perulangan

# The break statement
a = 10
while a > 5:
    print (a)
    if a == 8:  # Jika a = 8
        break   # Pengulangan berhenti
    a -= 1      # Mengurangi nilai a setiap perulangan

a = 10
while a > 0:
    print ("Nilai a:", a)
    if a == 4:
        print ("Loop berhenti")
        break
    a -= 2

# The continue Statement
a = 10
while a > 5:        # Perulangan berjalan selama a > 5
    a -= 2          # Setiap loop, nilai a dikurangi 2
    if a == 8:      # Jika a = 8
        continue    # Lewati perintah dan lanjut ke loop berikutnya
    print (a)       # Outputnya 6 4

# The else Statement
a = 10
while a > 5:
    print (a)
    a -= 2
else:               # Dijalankan jika while berhenti secara normal (kondisi a > 5 sudah bernilai False)
    print ("Loop selesai")

a = 10
while a > 0:
    print ("Nilai a:", a)
    if a == 4:
        print ("Loop berhenti")
        break
    a -= 2
else:
    print ("Loop selesai")