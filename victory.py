# Словарь с годами рождения известных людей
celebrities = {
    "Александр Сергеевич Пушкин": 1799,
    "Михаил Юрьевич Лермонтов": 1814,
    "Владимир Ильич Ленин": 1870,
    "Мария Склодовская-Кюри": 1867,
    "Альберт Эйнштейн": 1879
}

# Функция для проведения викторины
def run_quiz():
    correct_answers = 0
    incorrect_answers = 0

    # Проходим по каждой знаменитости в словаре
    for celebrity, birth_year in celebrities.items():
        user_answer = int(input(f"Когда родился {celebrity}? "))

        # Проверяем ответ пользователя
        if user_answer == birth_year:
            print("Верно!")
            correct_answers += 1
        else:
            print(f"Неверно. {celebrity} родился в {birth_year} году.")
            incorrect_answers += 1

    # Вычисляем и выводим статистику
    total_questions = correct_answers + incorrect_answers
    correct_percent = correct_answers * 100 / total_questions
    incorrect_percent = incorrect_answers * 100 / total_questions

    print(f"Количество правильных ответов: {correct_answers}")
    print(f"Количество ошибок: {incorrect_answers}")
    print(f"Процент правильных ответов: {correct_percent:.2f}%")
    print(f"Процент неправильных ответов: {incorrect_percent:.2f}%")

    # Спрашиваем, хочет ли пользователь начать игру сначала
    restart = input("Хотите начать игру сначала? (да/нет) ").lower()
    if restart == "да":
        run_quiz()
    else:
        print("Спасибо за игру!")

# Запускаем викторину
run_quiz()
