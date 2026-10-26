N = int(input("Введите N: "))

factorial = 1.0
while N > 0:
    factorial *= N
    N -= 2

print(f"Двойной факториал: {factorial}")