N = int(input("Введите N: "))

power = 1
K = 0
while power * 3 < N:
    power *= 3
    K += 1

print(f"Максимальное K: {K}")