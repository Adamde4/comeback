address_book = {}

# Функція для додавання нового контакту
def add_contact(name, phone, email):
    if name not in address_book:
        address_book[name] = {'phone': phone, 'email': email}
        print(f"Контакт '{name}' був доданий до адресної книги.")
    else:
        print(f"Контакт з іменем '{name}' вже існує.")


# Функція для видалення контакту
def delete_contact(name):
    if name in address_book:
        del address_book[name]
        print(f"Контакт '{name}' був видалений з адресної книги.")
    else:
        print(f"Контакт з іменем '{name}' не знайдений.")


# Функція для редагування контакту
def edit_contact(name, phone, email):
    if name in address_book:
        address_book[name]['phone'] = phone
        address_book[name]['email'] = email
        print(f"Контакт '{name}' був відредагований.")
    else:
        print(f"Контакт з іменем '{name}' не знайдений.")