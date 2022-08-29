# Задача 1. Задайте список случайных чисел от 1 до 10,
# выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random

# n = int(input("Введите число n: "))
# my_list = []
# for i in range(n):
#     my_list.append(random.randint(1,10))
# print(my_list)

my_list = [i for i in range(random.randint(1,10))]
print(my_list)

print(list(filter(lambda x: x>5, my_list)))