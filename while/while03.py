N = int(input("Введите N: "))
K = int(input("Введите K: "))

quotient = 0
remainder = N
while remainder >= K:
    remainder -= K
    quotient += 1

print(f"Частное: {quotient}")
print(f"Остаток: {remainder}")