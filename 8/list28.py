n = int(input())
s = []
for i in range(n):
    s.append(input())
letter = input()
print([w for w in s if w[0] == letter])
