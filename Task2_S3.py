# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, 
# названия которых начинаются на заданную букву.

fruites = ["apple", "orange", "peach", "pear"]
letter = input("Введите букву: ")
for i in range(len(fruites)):
    if fruites[i][0] == letter:
        print(fruites[i])
    