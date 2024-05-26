# Бесконечный цикл для ввода года рождения
while True:
    user_year = int(input("Введите год рождения А.С. Пушкина: "))
    if user_year == 1799:
        break
    else:
        print("Неверный год рождения")

# Бесконечный цикл для ввода месяца рождения
while True:
    user_month = int(input("Введите месяц рождения А.С. Пушкина: "))
    if user_month == 6:
        break
    else:
        print("Неверный месяц рождения")

# Бесконечный цикл для ввода дня рождения
while True:
    user_day = int(input("Введите день рождения А.С. Пушкина: "))
    if user_day == 6:
        print("Верно")
        break
    else:
        print("Неверный день рождения")
