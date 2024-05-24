def palindrome(x):
    x=x.lower().replace(" ", "")
    return x == x[::-1]

# Driver Code
x = input("Masukkan sebuah kalimat: ")
if palindrome(x):
    print("Palindrom")
else:
    print("Bukan palindrom")