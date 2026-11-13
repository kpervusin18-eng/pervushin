n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
inv = {}
for key, value in d.items():
    inv[value] = key
for key, value in inv.items():
    print(key, value)
