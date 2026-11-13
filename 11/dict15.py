n = int(input())
d1 = {}
for i in range(n):
    key = input()
    value = int(input())
    d1[key] = value
m = int(input())
d2 = {}
for i in range(m):
    key = input()
    value = int(input())
    d2[key] = value
ignored = 0
for key in d2:
    if key in d1:
        ignored += 1
    else:
        d1[key] = d2[key]
print(len(d1))
print(ignored)
