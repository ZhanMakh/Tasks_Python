# Задача 3. Даны две строки. Посчитайте сколько раз каждый 
# символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

string1 = input("Введите слово: ")
string2 = "onetownine"
count = 0
for i in range(len(string1)):
    for j in range(len(string2)):
        if string1[i] == string2[j]:
            count +=1
    print(f"буква {string1[i]} встречается {count} раза")
    count = 0