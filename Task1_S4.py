# Задача 1. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

N = int(input("Введите любое число: "))
i=2
while i<=N:
    while N%i==0:
        print(i, end=" ")
        N//=i
    i+=1