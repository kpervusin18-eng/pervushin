N = int(input("Введите N: "))

power = 1
K = 0
while power <= N:
    power *= 3
    K += 1

print(f"Минимальное K: {K}")