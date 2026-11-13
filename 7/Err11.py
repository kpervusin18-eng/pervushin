try:
    a = int(input())
    b = int(input())
    result = a/b
except (ValueError, ZeroDivisionError):
    print("Посчитать не удалось")
else:
    print(f"{result:.2f}")