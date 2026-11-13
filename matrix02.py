m = int(input())
n = int(input())
a = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(5 * (j + 1))
    a.append(row)
for row in a:
    print(row)
