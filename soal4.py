def jumlah_digit( x ):
	if x == 0:
		return 0
	return (x % 10 + jumlah_digit(int(x / 10)))

angka = 234
result = jumlah_digit(angka)
print("jumlah digit",angka,"adalah", result)