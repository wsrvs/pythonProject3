# Запрашиваем ввод года рождения от пользователя
user_year = int(input("Введите год рождения А.С. Пушкина: "))

# Проверяем правильность введенного года
if user_year == 1799:
    # Год введен верно, запрашиваем ввод месяца рождения
    user_month = int(input("Введите месяц рождения А.С. Пушкина: "))

    # Проверяем правильность введенного месяца
    if user_month == 6:
        # Месяц введен верно, запрашиваем ввод дня рождения
        user_day = int(input("Введите день рождения А.С. Пушкина: "))

        # Проверяем правильность введенного дня
        if user_day == 6:
            print("Верно")
        else:
            print("Неверный день рождения")
    else:
        print("Неверный месяц рождения")
else:
    print("Неверный год рождения")

