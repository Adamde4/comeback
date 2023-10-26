numbers = []  #список чисел

try:
    n = int(input("Скільки чисел бажаєте ввести? "))
    for i in range(n):
        num = float(input(f"Введіть число {i + 1}: "))
        numbers.append(num)
    print(f"Ваші числа: {numbers}")
except ValueError:
    print("Помилка: некоректно введені дані.")

if len(numbers) > 0:  # Переконайтеся, що список не є порожнім перед обчисленням середнього
    total = sum(numbers)
    average = total / n
    print(f"Середнє значення: {average}")
else:
    print("Немає чисел для обчислення середнього.")
