# Задача:
#
# Реализуйте паттерн Proxy для контроля доступа к объекту банка,
# который содержит информацию о банковских счетах клиентов.
#
# Шаги:
# Создайте класс для управления банковскими счетами.
# Создайте класс заместителя, который контролирует доступ к банковскому классу.
# Реализуйте методы для проверки доступа и выполнения операций.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance


class BankAccountProxy:
    def __init__(self, account, user):
        self._account = account
        self._user = user

    def deposit(self, amount):
        self._check_access()
        return self._account.deposit(amount)

    def withdraw(self, amount):
        self._check_access()
        return self._account.withdraw(amount)

    def _check_access(self):
        if self._user != self._account.owner:
            raise PermissionError("Unauthorized access")


def main():
    # Тестирование
    account = BankAccount("Alice", 1000)
    proxy = BankAccountProxy(account, "Alice")

    print(proxy.deposit(500))  # Output: 1500
    print(proxy.withdraw(200))  # Output: 1300

    proxy_wrong_user = BankAccountProxy(account, "Bob")
    proxy_wrong_user.deposit(100)  # Raises PermissionError


if __name__ == "__main__":
    main()
