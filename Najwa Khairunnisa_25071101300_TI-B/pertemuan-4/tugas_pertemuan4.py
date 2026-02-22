'''
Najwa membuat program untuk menghitung IPK Sementara. Program akan meminta pengguna untuk:
1.	Memasukkan jumlah mata kuliah yang diambil
2.	Memasukkan total SKS
3.	Memasukkan total bobot nilai (hasil nilai x SKS masing-masing mata kuliah)
Rumus IPK:
IPK = total bobot nilai ÷ total SKS
Namun, terjadi beberapa kemungkinan masalah:
1.	Input tidak valid
2.	Pembagian dengan nol
'''

try:
    jumlah_mata_kuliah = int(input("Jumlah mata kuliah yang diambil: "))
    total_sks = int(input("Total SKS: "))
    total_bobot_nilai = float(input("Total bobot nilai: "))

    if jumlah_mata_kuliah <= 0:
        print("Jumlah mata kuliah harus lebih dari 0")

    elif total_sks <= 0:
        print("Totak SKS harus lebih dari 0")

    elif total_bobot_nilai <= 0:
        print("Total bobot harus lebih dari 0")

    else:
        ipk = total_bobot_nilai / total_sks
        print("IPK Sementara:", ipk)

except ValueError:
    print("Input harus angka")

except ZeroDivisionError:
    print("Pembagian tidak boleh 0")