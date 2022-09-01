# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, 
# знаменатель которых не превышает 11.

# n = int(input("Введите число: "))
# data=[]
for i in range(1, 13, 2):
    for j in range(1, 12):
        if i/j < 1:
            if j/i != 0 and j%i != 0:
                print(f"{i}/{j}", end=" ")
for i in range(2, 13, 2):
    for j in range(3, 12, 2):
        if i/j < 1:
            if j/i != 0 and j%i != 0:
                print(f"{i}/{j}", end=" ")

