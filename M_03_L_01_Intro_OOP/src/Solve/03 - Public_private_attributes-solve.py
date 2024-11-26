# Ex 1
# Создайте класс `BankAccount` с публичным атрибутом `owner` и приватным атрибутом `__balance`.
# Реализуйте методы для внесения депозита и снятия денег, обеспечивая корректность операций
# (например, нельзя снять больше, чем есть на балансе).
#
# Ex 2
# Создайте класс `Product` с публичным атрибутом `name` и приватным атрибутом `__price`.
# Реализуйте методы для получения и изменения цены,
# добавив проверки на корректность (цена не может быть отрицательной).

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        """Инициализация банковского аккаунта."""
        self.owner = owner  # Публичный атрибут
        self.__balance = initial_balance  # Приватный атрибут

    def deposit(self, amount):
        """Внесение депозита на счет."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Снятие денег со счета."""
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")

    def get_balance(self):
        """Получение текущего баланса."""
        return self.__balance


class Product:
    def __init__(self, name, price):
        """Инициализация продукта с именем и ценой."""
        self.name = name  # Публичный атрибут
        self.__price = None  # Приватный атрибут
        self.set_price(price)  # Устанавливаем цену через метод, чтобы применить проверки

    def get_price(self):
        """Возвращает текущую цену продукта."""
        return self.__price

    def set_price(self, price):
        """Устанавливает новую цену продукта с проверкой на корректность."""
        if price < 0:
            print("Price cannot be negative.")
        else:
            self.__price = price
            print(f"Price for {self.name} set to {self.__price}")


def main():
    print("Bank Account Example:")
    # Пример использования:
    # Создаем банковский счет
    account = BankAccount("Alice", 100)

    # Проверяем баланс
    print(f"Owner: {account.owner}")
    print(f"Initial Balance: {account.get_balance()}")

    # Вносим депозит
    account.deposit(50)

    # Пытаемся снять сумму больше, чем доступно
    account.withdraw(200)

    # Снимаем доступную сумму
    account.withdraw(30)

    # Проверяем текущий баланс
    print(f"Final Balance: {account.get_balance()}")

    print("\nProduct Example:")
    # Пример использования:
    # Создаем продукт
    product = Product("Laptop", 1000)

    # Получаем цену
    print(f"Current price of {product.name}: {product.get_price()}")

    # Устанавливаем новую цену
    product.set_price(1200)

    # Пытаемся установить отрицательную цену
    product.set_price(-500)

    # Получаем текущую цену после попытки некорректного изменения
    print(f"Final price of {product.name}: {product.get_price()}")


if __name__ == "__main__":
    main()
