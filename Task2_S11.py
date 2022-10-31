# Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимость квадратного метра каждого дома и список 
# подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. 
# Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

import random
import matplotlib.pyplot as m

square = []
for i in range(15):
    square.append(random.randint(100,300))

price_house = []
for i in range(15):
    price_house.append(random.randint(3000000,20000000))

cost_metr = list(round(price_house[i]/square[i],0) for i in range(15))
m.plot(cost_metr, square,"ro")
m.show()