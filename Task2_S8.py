# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

import random
str = 3
col = 3
Massiv = ["0"]*str
for i in range(len(Massiv)):
    Massiv[i] = list(Massiv[i]) * col

for i in range(str):
    for j in range(col):
        Massiv[i][j] = random.randint(1,5)
for i in Massiv:
    print(i)

print()
res = [0]* str
for i in range(str):
    d = 0
    for j in range(len(res)):
        sum = 0
        for k in range(col):
            sum = sum + Massiv[j][k]
            if k == j:
                d = d + Massiv [k][k]
        res[j] = sum
#print (res, d)
    
    if res[i] > d:
        print (f"Сумма в {i+1} строке равна {res[i]} и она больше, чем сумма чисел по диагонали, равной {d}")
    #else:
        #print (f"Сумма чисел по диагонали равна {d} и она больше суммы чисел в каждой строке")
        
   


