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
d1.update(d2)
common = None
for key in d2:
    if key in d2:
        common = key
print(len(d1))
print(d1[common])
