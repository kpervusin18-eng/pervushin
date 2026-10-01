n = int(input())
total = 0.0
sign = 1
for i in range(1, n + 1):
    term = 1 + i / 10
    total += sign * term
    sign *= -1
print(total)
