# Задача 1. Напишите программу, которая принимает на вход число N 
# и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def myFactorial(x):
    count = 1
    for i in range(1,x+1):
        count = count * i
    return count

N = int(input("введите число: "))
result = [0] *N
for i in range(len(result)):
    result[i] = myFactorial(i+1)
print(result)
