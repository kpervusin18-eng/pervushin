A = int(input("Введите A: "))
B = int(input("Введите B: "))

free_part = A
while free_part >= B:
    free_part -= B

print(f"Длина незанятой части: {free_part}")