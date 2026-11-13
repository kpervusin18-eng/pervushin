m = int(input())
n = int(input())
q = int(input())
values = [int(x) for x in input().split()]
a = []
power = 1
for i in range(m):
    row = [x * power for x in values]
    a.append(row)
    power = power * q
for row in a:
    print(row)
