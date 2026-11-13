n = int(input())
d = {}
for i in range(n):
    name = input()
    price = int(input())
    qty = int(input())
    d[name] = [price, qty]
total = 0
best_name = None
for name, pair in d.items():
    price, qty = pair
    cost = price * qty
    total += cost
    if best_name is None or cost > d[best_name][0] * d[best_name][1]:
        best_name = name
print(total)
print(best_name)
