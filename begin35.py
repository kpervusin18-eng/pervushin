v = float(input())
u = float(input())
t1 = float(input())
t2 = float(input())

s_lake = v * t1
s_river = (v - u) * t2
total_distance = s_lake + s_river

print(total_distance)
