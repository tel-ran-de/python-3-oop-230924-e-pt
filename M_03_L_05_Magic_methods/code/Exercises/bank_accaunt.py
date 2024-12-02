# Создайте класс BankAccount, который будет представлять банковский счет. Класс должен включать следующие функции:
#
# Инкапсуляция: Приватные атрибуты для номера счета и баланса.
# Конструктор: Метод для инициализации объекта с номером счета и начальным балансом.
# Геттеры и сеттеры: Методы для доступа и изменения баланса.
# Магические методы: Методы для добавления и снятия денег (__add__ и __sub__),
# сравнения балансов (__eq__, __lt__, __le__, и т.д.), строкового представления (__str__ и __repr__),
# и вызова объекта (__call__).

class BankAccount:
    pass


def main():
    # Тестирование
    account1 = BankAccount("12345678", 1000.0)
    account2 = BankAccount("87654321", 500.0)

    # Инкапсуляция и доступ к атрибутам через геттеры и сеттеры
    print(account1.balance)  # Output: 1000.0
    account1.balance = 1200.0
    print(account1.balance)  # Output: 1200.0

    # Попытка установить отрицательный баланс вызывает ошибку
    # account1.balance = -500.0  # Raises ValueError

    # Использование методов для внесения и снятия средств
    account1.deposit(300.0)
    print(account1.balance)  # Output: 1500.0
    account1.withdraw(200.0)
    print(account1.balance)  # Output: 1300.0

    # Использование магических методов для арифметических операций
    account1 + 500.0
    print(account1.balance)  # Output: 1800.0
    account1 - 300.0
    print(account1.balance)  # Output: 1500.0

    # Сравнение счетов
    print(account1 == account2)  # Output: False
    print(account1 > account2)  # Output: True

    # Представление объекта
    print(account1)  # Output: BankAccount(account_number=12345678, balance=1500.0)
    print(repr(account1))  # Output: BankAccount(account_number=12345678, balance=1500.0)

    # Вызов объекта
    account1()  # Output: Account 12345678 has a balance of 1500.0


if __name__ == "__main__":
    main()

# 1000.0
# 1200.0
# 1500.0
# 1300.0
# 1800.0
# 1500.0
# False
# True
# BankAccount(account_number=12345678, balance=1500.0)
# BankAccount(account_number=12345678, balance=1500.0)
# Account 12345678 has a balance of 1500.0
