# Ex 1
# Создайте класс `Library`, у которого будет атрибут класса `total_books` и
# атрибут объекта `books` (список книг в данной библиотеке).
# Реализуйте методы для добавления книги в библиотеку и вывода общего количества книг во всех библиотеках.
#
# Ex 2
# Создайте класс `Company` с атрибутом класса `company_name` и
# атрибутом объекта `employees` (список сотрудников).
# Реализуйте методы для добавления сотрудника и вывода списка всех сотрудников данной компании.

class Library:
    # Атрибут класса для хранения общего количества книг
    total_books = 0

    def __init__(self):
        # Атрибут объекта для хранения списка книг в данной библиотеке
        self.books = []

    def add_book(self, book):
        """Добавляет книгу в библиотеку и обновляет общий счетчик книг."""
        self.books.append(book)
        Library.total_books += 1

    @classmethod
    def get_total_books(cls):
        """Возвращает общее количество книг во всех библиотеках."""
        return cls.total_books



class Company:

    def __init__(self, name):
        # Устанавливаем имя компании при создании объекта
        Company.company_name = name
        # Атрибут объекта для хранения списка сотрудников
        self.employees = []

    def add_employee(self, employee_name):
        """Добавляет сотрудника в список сотрудников компании."""
        self.employees.append(employee_name)

    def list_employees(self):
        """Возвращает список всех сотрудников данной компании."""
        return self.employees


def main():
    # Пример использования:
    print("Library class example")
    # Создаем библиотеки
    library1 = Library()
    library2 = Library()

    # Добавляем книги в первую библиотеку
    library1.add_book("1984")
    library1.add_book("To Kill a Mockingbird")

    # Добавляем книгу во вторую библиотеку
    library2.add_book("Brave New World")

    # Выводим общее количество книг
    print(f"Total books in all libraries: {Library.get_total_books()}")  # Output: 3

    # Выводим книги в каждой библиотеке
    print(f"Books in library1: {library1.books}")  # Output: ['1984', 'To Kill a Mockingbird']
    print(f"Books in library2: {library2.books}")  # Output: ['Brave New World']
    #
    # # Пример использования:
    # print("\nCompany class example")
    # # Создаем компанию
    # company = Company("TechCorp")
    #
    # # Добавляем сотрудников
    # company.add_employee("Alice")
    # company.add_employee("Bob")
    # company.add_employee("Charlie")
    #
    # # Выводим название компании
    # print(f"Company name: {Company.company_name}")  # Output: TechCorp
    #
    # # Выводим список сотрудников
    # print(f"Employees: {company.list_employees()}")  # Output: ['Alice', 'Bob', 'Charlie']


if  __name__ == "__main__":
    main()
