# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
# Список уникальных элементов [1, 4, 2, 3, 6, 7]

import random

n = int(input("Введите число n: "))
my_list = []
for i in range(n):
    my_list.append(random.randint(1,10))
print(my_list)

sum = 0
for i in my_list:
    if my_list.count(i) != 1:
        sum +=1
print(f"в списке совпадающих элементов {sum} раз")

data = set(my_list)
print(data)
