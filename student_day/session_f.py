
# Функція для обчислення середнього рейтингу
def average_rating(ratings):
    total = sum(ratings.values())  # Знайдемо суму всіх оцінок
    count = len(ratings)  # Знайдемо кількість студентів
    average_score = total / count
    return average_score  # Обчислимо середній рейтинг
    # Викличемо функцію для обчислення середнього рейтингу


# Функція для знаходження студента з найвищим рейтингом
def max_score(ratings):
    top_student = max(ratings, key=ratings.get)  # Знайдемо студента з максимальним рейтингом
    top_score = ratings[top_student]  # Знайдемо його рейтинг
    return top_student, top_score  # Повернемо ім'я та рейтинг


def min_score(ratings):
    bad_student = min(ratings, key=ratings.get)  # Знайдемо студента з мінімальним рейтингом
    bad_score = ratings[bad_student]  # Знайдемо його рейтинг
    return bad_student, bad_score  # Повернемо ім'я та рейтинг

def get_status(name, rating):
    if rating < 65:
        return f"{name}: Виключення"
    elif rating > 90:
        return f"{name}: Медаль"
    else:
        return f"{name}: Звичайний студент"
