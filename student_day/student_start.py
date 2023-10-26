from student_start_f import add_contact
from student_start_f import delete_contact
from student_start_f import edit_contact

address_book = {}

# Головний цикл програми
while True:
    print("\nОберіть дію:")
    print("1. Додати контакт")
    print("2. Видалити контакт")
    print("3. Редагувати контакт")
    print("4. Показати всі контакти")
    print("5. Вийти")

    choice = input("Ваш вибір: ")

    if choice == '1':
        name = input("Введіть ім'я контакту: ")
        phone = input("Введіть номер телефону: ")
        email = input("Введіть електронну адресу: ")
        add_contact(name, phone, email)
    elif choice == '2':
        name = input("Введіть ім'я контакту, який потрібно видалити: ")
        delete_contact(name)
    elif choice == '3':
        name = input("Введіть ім'я контакту, який потрібно відредагувати: ")
        phone = input("Введіть новий номер телефону: ")
        email = input("Введіть нову електронну адресу: ")
        edit_contact(name, phone, email)
    elif choice == '4':
        print("Список всіх контактів:")
        for name, info in address_book.items():
            print(f"Ім'я: {name}, Телефон: {info['phone']}, Email: {info['email']}")
    elif choice == '5':
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")