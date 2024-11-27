class PositiveNumber:
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be non-negative")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class BankAccount:
    balance = PositiveNumber()

    def __init__(self, balance):
        self.balance = balance


def main():
    # Использование
    account = BankAccount(100)
    print(account.balance)  # Output: 100

    try:
        account.balance = -50
    except ValueError as e:
        print(e)  # Output: Value must be non-negative


if __name__ == "__main__":
    main()
