def triangle_p(a, h):
    b = ((a / 2) ** 2 + h ** 2) ** 0.5
    return a + 2 * b
for i in range(3):
    a = float(input())
    h = float(input())
    print(triangle_p(a, h))
