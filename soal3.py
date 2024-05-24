def deret_ganjil_faktorial(n):
    if n == 1:
        return 1
    else:
        faktorial = 1
        for i in range(1, n + 1):
            faktorial *= i

        return faktorial + deret_ganjil_faktorial(n - 2)

angka = 7
hasil = deret_ganjil_faktorial(angka)
print("Jumlah deret ganjil hingga", angka, "adalah", hasil)
