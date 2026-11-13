n = int(input())
s = []
for i in range(n):
    s.append(input())
print([len(w) for w in s])
print(sum(len(w) for w in s))
