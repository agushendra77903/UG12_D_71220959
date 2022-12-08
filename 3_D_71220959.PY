print("~~~~Table Matematika Nich~~~~ \n pilihan model matematika")
print("1.perkalian")
print("2.pembagian")
kata = int(input("masukkan model matematika yang di inginkan 1/2:"))
if kata == 1:
    numbers= int(input("menampilkan tabel matematika dari angka : "))
    for i in range(1, 11):
        print(numbers, 'x', i, '=', numbers*i)

elif kata == 2:
    numbers= int(input("menampilkan tabel matematika dari angka : "))
    for i in range (50, 66):
        print(numbers,':', i, '=', i/numbers )

else:
    print("tidak tersedia, jangan ngasal ngab!")
