n = 10  # Задаем количество строк (количество уровней пирамиды)

for i in range(1, n, 2):
    for j in range(i):
        print("*", end=" ")  # Выводим звездочку и пробел после неё
    print()  # Переходим на новую строку после каждой строки звездочек
