# Задача 2. Дан список случайных чисел. 
# Создайте список, в который попадают числа, описывающие 
# возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

import random

n = int(input("Введите число n: "))
my_list = []
for i in range(n):
    my_list.append(random.randint(1,10))
print(my_list)

data = sorted(my_list)
print(data)

print(f"ответ: {data[2:]} или {data[3:n]} или {data[:n-2]}")