# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

N = int(input("Введите число N: "))
interval = list(range(-N,N+1))
step = 2
print (interval)

print(interval[:-step])
print(interval[-step:])
print (interval[-step:]+interval[:-step])


