# Задача 1. В каждой группе учится от 20 до 30 студентов. 
# По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

import random

str = 3
col = 20
Massiv = ["0"]*str
for i in range(len(Massiv)):
    Massiv[i] = list(Massiv[i]) * col

for i in range(len(Massiv)):
    for j in range(len(Massiv[i])):
        Massiv[i][j] = random.randint(1,5)
for i in Massiv:
    print(i)

res = [0,0,0]
for i in range(len(Massiv)):
    for j in range(len(res)):
        sum = 0
        for k in range(len(Massiv[j])):
            sum = sum + Massiv[j][k]
        res[j] = round (sum/col, 2)
        
print (res)

max = res[1]
for i in range(len(res)):
    if res[i]>=max:
        max = res[i]
        j = i+1

print (f"лучший результат в {j} группе, где средний бал равен {max}")