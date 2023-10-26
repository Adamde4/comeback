from session_f import average_rating
from session_f import max_score
from session_f import min_score
from session_f import get_status
# Викличемо функцію для знаходження середнього рейтингу

student_ratings = {
    'John': 90,
    'Alice': 85,
    'Mike': 60,
    'Bob': 78,
    'Eva': 92,}

average = average_rating(student_ratings)

# Викличемо функцію для знаходження студента з найвищим рейтингом
top_student = max_score(student_ratings)

# Викличемо функцію для знаходження студента з найвищим рейтингом
bad_student = min_score(student_ratings)


# Виведемо результат
print(f"Середній рейтинг студентів: {average}",
      f"Максимальний бал: {top_student}",
      f"Мінімальний бал: {bad_student}")

# Пройдіться по словнику та визначте статус для кожного студента
for name, rating in student_ratings.items():
    status = get_status(name, rating)
    print(status)