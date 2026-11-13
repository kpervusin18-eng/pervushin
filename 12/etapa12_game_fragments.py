# -*- coding: utf-8 -*-
# Этап 12. Меню понимает команды. Фрагменты для вставки в game.py.
# Все фрагменты согласованы с кодом этапов 10-11 (fight, buy, inventory).

# ---------- БЛОК 1. Командная строка: нормализация и глагол ----------

# 1. До главного цикла (рядом с prices и enemy_stats):
num_to_verb = {"1": "look", "2": "go", "3": "rest", "4": "listen",
               "5": "torch", "6": "train", "7": "descend", "8": "leaders",
               "9": "shop", "10": "backpack", "11": "drink", "0": "exit"}

# 2. Чтение команды внутри главного цикла (вместо числовой проверки урока 6;
#    menu_last больше не нужен):
line = input()
cmd = line.strip().lower()
while cmd == "":
    print("Empty command. Type a command or number.")
    line = input()
    cmd = line.strip().lower()
words = cmd.split()
verb = words[0]
if cmd in num_to_verb:
    verb = num_to_verb[cmd]

# 3. match переключается с номеров на глаголы; тела веток переезжают
#    без изменений:
# match verb:
#     case "look":  ...прежнее тело пункта 1...
#     case "go":    ...прежнее тело пункта 2...
#     case "rest":  ...прежнее тело пункта 3...
#     case "exit":
#         print("You climb back toward the light. The dungeon stays behind.")
#         outcome = "exit"
#         running = False
#     case "help":   ...блок 3...
#     case "buy":    ...блок 2...
#     case "drink":  ...блок 2...
#     case _:        ...блок 4...
# Ветки shop / backpack / descend / leaders / torch / train / listen
# переезжают в case со своим прежним телом (см. файл целиком ниже).


# ---------- БЛОК 2. Команды с дополнением: buy и drink ----------

# Ветка покупки внутри match verb. Порядок важен: сначала количество,
# потом имя, иначе "buy potion 2" дал бы имя "potion 2".
#     case "buy":
#         if len(words) > 1 and words[-1].isdigit():
#             qty = int(words[-1])
#             item = " ".join(words[1:-1])
#         else:
#             qty = 1
#             item = " ".join(words[1:])
#         if item == "":
#             print("Buy what? Type: buy <item>.")
#             continue
#         if item not in prices:
#             print("No such item in the shop.")
#             continue
#         gold_total, ok = buy(prices[item], gold_total, quantity=qty)
#         if ok:
#             inventory[item] = inventory.get(item, 0) + qty
#             print(f"Bought {qty} {item} for {prices[item] * qty} gold. "
#                   f"Gold left: {gold_total}.")
#         else:
#             print(f"Not enough gold: need {prices[item] * qty}, "
#                   f"have {gold_total}.")

# Ветка питья: пустая склейка даёт пустую строку, or подставляет "potion"
# (короткое замыкание из занятия 3):
#     case "drink":
#         item = " ".join(words[1:]) or "potion"
#         if inventory.get(item, 0) == 0:
#             print(f"No {item} in the backpack.")
#         else:
#             health = min(health + 10, max_health)
#             inventory[item] -= 1
#             if inventory[item] == 0:
#                 del inventory[item]
#             print(f"You drink a {item}. Health: {health}. "
#                   f"Potions left: {inventory.get(item, 0)}.")

# Ветка case "shop" по-прежнему печатает прейскурант перебором items.


# ---------- БЛОК 3. Справка и меню через join ----------

commands = ["look", "go", "rest", "listen", "torch", "train", "descend",
            "leaders", "shop", "backpack", "drink potion",
            "buy <item> [count]", "exit"]
MENU = ["What do you do? (number or command; help for help)",
        "1 - look around (look)",
        "2 - go forward (go)",
        "3 - rest (rest)",
        "4 - listen (listen)",
        "5 - light a torch (torch)",
        "6 - train (train)",
        "7 - descend deeper (descend)",
        "8 - leaderboard (leaders)",
        "9 - shop (shop)",
        "10 - backpack (backpack)",
        "11 - drink potion (drink)",
        "0 - exit the dungeon (exit)"]

# Меню внутри цикла одним join вместо тринадцати print:
# print("\n".join(MENU))
# print()

# Ветка справки:
#     case "help":
#         print("Commands: " + ", ".join(commands) + ".")
#         print("Numbers 0-11 work as before.")
#
# Новый пункт правится в ТРЁХ местах: строка в MENU, пара в num_to_verb,
# ветка match. Забытый num_to_verb - частая болезнь этого блока.


# ---------- БЛОК 4. Незнакомая команда и учёт кругов ----------

# Ветка цитирует исходную строку line, а не нормализованную cmd:
#     case _:
#         print(f"Don't understand command: '{line.strip()}'. Type 'help'.")
#         continue
#
# continue пропускает счётчик действий и строку состояния: неизвестная
# команда не тратит игровой круг. help и состоявшиеся команды считаются
# действиями, отказы ("Buy what?", "No such item...") и "не понимаю" - нет.
# Счётчик действий, строка состояния и проверка гибели не меняются:
# они стоят после match.

# ---------- .gitignore (отдельный коммит "Git: ignore service files") ----------
# __pycache__/
# *.save
