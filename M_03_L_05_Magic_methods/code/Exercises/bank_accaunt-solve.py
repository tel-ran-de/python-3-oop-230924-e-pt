# Создайте класс BankAccount, который будет представлять банковский счет. Класс должен включать следующие функции:
#
# Инкапсуляция: Приватные атрибуты для номера счета и баланса.
# Конструктор: Метод для инициализации объекта с номером счета и начальным балансом.
# Геттеры и сеттеры: Методы для доступа и изменения баланса.
# Магические методы: Методы для добавления и снятия денег (__add__ и __sub__),
# сравнения балансов (__eq__, __lt__, __le__, и т.д.), строкового представления (__str__ и __repr__),
# и вызова объекта (__call__).

class BankAccount:
    def __init__(self, account_number, initial_balance=0.0):
        self.__account_number = account_number  # Приватный атрибут
        self.__balance = initial_balance  # Приватный атрибут

    # Геттер для получения баланса
    @property
    def balance(self):
        return self.__balance

    # Сеттер для установки баланса
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

    # Метод для добавления денег
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    # Метод для снятия денег
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    # Магические методы для арифметических операций
    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        self.withdraw(amount)
        return self

    # Магические методы для сравнения
    def __eq__(self, other):
        return self.__balance == other.__balance

    def __lt__(self, other):
        return self.__balance < other.__balance

    def __le__(self, other):
        return self.__balance <= other.__balance

    # Магические методы для представления объекта
    def __str__(self):
        return f"BankAccount(account_number={self.__account_number}, balance={self.__balance})"

    def __repr__(self):
        return f"BankAccount(account_number={self.__account_number}, balance={self.__balance})"

    # Магический метод для вызова объекта
    def __call__(self):
        print(f"Account {self.__account_number} has a balance of {self.__balance}")


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
