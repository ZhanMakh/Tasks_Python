# Задача 1. Создайте файл. 
# Запишите в него N первых элементов последовательности Фибоначчи.

def myFibonacci(x):
    if x in [1,2]:
        return 1
    else:
        return myFibonacci(x-1)+myFibonacci(x-2)

data = open("fibon.txt","w")

list=[]
for y in range(1,6):
    list.append(myFibonacci(y))

data.writelines(str(list))
data.close


# fib = [1,1,2,3,5]
# with open("fibon.txt", "w") as data:
#     data.write("1\n")
#     data.write("1\n")
#     data.write("2\n")
#     data.write("3\n")
#     data.write("5\n")
