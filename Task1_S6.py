# Задача 1. Дано натуральное число N. Найдите значение выражения:
# N + NN + NNN. N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

N= int(input("Введите любое число N: "))
x1 = str(N)
x2 = str(N) + str(N)
x3 = str(N) + str(N) + str(N)
y1 = int(x1)
y2 = int(x2)
y3 = int(x3)
sum = y1 + y2 + y3
print (sum)
