# Задача 1: Создание класса Student с использованием декоратора property
# Описание:
#
# Создайте класс Student, который будет иметь приватные атрибуты name и grade.
# Реализуйте геттеры и сеттеры для этих атрибутов с использованием декоратора property.
#
# Требования:
#
# Приватные атрибуты __name и __grade.
# Свойства name и grade с геттерами и сеттерами.
# В сеттере для grade реализуйте проверку, что оценка должна быть в диапазоне от 0 до 100.
#
# Задача 2: Создание класса BankAccount с использованием декоратора property
# Описание:
#
# Создайте класс BankAccount, который будет иметь приватные атрибуты account_number и balance.
# Реализуйте геттеры и сеттеры для этих атрибутов с использованием декоратора property.
#
# Требования:
#
# Приватные атрибуты __account_number и __balance.
# Свойства account_number и balance с геттерами и сеттерами.
# В сеттере для balance реализуйте проверку, что баланс не может быть отрицательным.


class Student:
    pass


class BankAccount:
    pass


def main():
    # Создание объекта Student
    student = Student("Alice", 85)

    # Доступ и изменение атрибута name
    print(student.name)  # Output: Alice
    student.name = "Bob"
    print(student.name)  # Output: Bob

    # Доступ и изменение атрибута grade
    print(student.grade)  # Output: 85
    student.grade = 90
    print(student.grade)  # Output: 90

    # Проверка валидации оценки
    try:
        student.grade = 105
    except ValueError as e:
        print(e)  # Output: Grade must be between 0 and 100

    # Создание объекта BankAccount
    account = BankAccount("12345678", 1000)

    # Доступ и изменение атрибута account_number
    print(account.account_number)  # Output: 12345678
    account.account_number = "87654321"
    print(account.account_number)  # Output: 87654321

    # Доступ и изменение атрибута balance
    print(account.balance)  # Output: 1000
    account.balance = 1500
    print(account.balance)  # Output: 1500

    # Проверка валидации баланса
    try:
        account.balance = -500
    except ValueError as e:
        print(e)  # Output: Balance must be non-negative


if __name__ == "__main__":
    main()

# Alice
# Bob
# 85
# 90
# Grade must be between 0 and 100
# 12345678
# 87654321
# 1000
# 1500
# Balance must be non-negative
