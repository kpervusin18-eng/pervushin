N = int(input())
total = 0
K = 0
while total < N:
    K += 1
    total += K
print(f"Минимальное K: {K}")
print(f"Полученная сумма: {total}")