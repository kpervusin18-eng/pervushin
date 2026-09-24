import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
dx = x2 - x1
dy = y2 - y1
distance = math.sqrt(dx ** 2 + dy ** 2)
print(distance)
