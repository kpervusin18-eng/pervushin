alphabet = "abcdefghijklmnopqrstuvwxyz" + "абвгдежзийклмнопрстуфхцчшщъыьэюя"
s = input()
count = 0
for ch in s:
    if ch in alphabet:
        count += 1
print(count)
