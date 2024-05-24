def kombinasi(n, r):
    if r == 0 or n == r:
        return 1
    else:
        return kombinasi(n-1, r-1) + kombinasi(n-1, r)

n = 5
r = 2
hasil = kombinasi(n, r)
print("Kombinasi dari", n, "dan", r, "adalah", hasil)
