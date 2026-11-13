word = input()
try:
    index = int(input())
    print(word[index])
except IndexError:
    print("Нет такого символа")