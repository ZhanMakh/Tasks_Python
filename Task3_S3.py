# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре.
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут».
# Если фраза ему неизвестна, он выводит соответствующую фразу.

d = \
    {
        "Hello": "Hi",
        "What is your name": "Kate",
        "Can I help you": "Yes",
        "See you later": "by-by"
    }

def bot():
    key= ""
    while key != "See you later":
        key = str(input("you: "))
        if key in d:
            print(f"bot: {d[key]}")
        else:
            print("dfg")
bot()
