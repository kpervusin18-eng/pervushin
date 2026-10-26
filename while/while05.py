N = int(input("Введите N: "))

power = 0
while N > 1:
    N //= 2
    power += 1

print(f"Показатель степени: {power}")