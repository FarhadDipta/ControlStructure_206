n = int(input("Masukkan nilai n: "))

a, b = 0, 1
print("Deret Fibonacci hingga", n, ":")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
