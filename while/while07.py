N = int(input("Введите N: "))

K = 1
while K * K <= N:
    K += 1

print(f"Минимальное K: {K}")