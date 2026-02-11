import myOOP

y = myOOP.ProdukElektronik("TV", "3.000.000", 2)
y.info_produk()

x = myOOP.ProdukMakanan("Roti", "15.000", "12-12-2026")
x.info_produk()

a = myOOP.Email("Email terkirim")
a.kirim()

b = myOOP.SMS("SMS terkirim")
b.kirim()

z = myOOP.Mahasiswa(100)
print(z.set_nilai(-5))