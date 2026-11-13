def minmax(x, y):
    if x < y:
        return x, y
    return y, x
a = float(input())
b = float(input())
c = float(input())
d = float(input())
mn1, mx1 = minmax(a, b)
mn2, mx2 = minmax(c, d)
mn, _ = minmax(mn1, mn2)
_, mx = minmax(mx1, mx2)
print(mn)
print(mx)
