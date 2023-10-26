class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Книга: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Рік видання: {self.year}")

# Створіть об'єкт класу Book
book1 = Book("Кобзар", "Тарас Шевченко", "1838-1840")

# Викличте метод для виведення інформації про книгу
book1.display_info()
