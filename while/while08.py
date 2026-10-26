N = int(input("Введите N: "))

K = 0
while (K + 1) * (K + 1) <= N:
    K += 1

print(f"Максимальное K: {K}")