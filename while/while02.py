A = int(input("Введите A: "))
B = int(input("Введите B: "))

count = 0
while A >= B:
    A -= B
    count += 1

print(f"Количество отрезков: {count}")