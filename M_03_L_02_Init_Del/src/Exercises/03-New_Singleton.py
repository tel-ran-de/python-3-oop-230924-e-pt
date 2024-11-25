# Задание 1: Реализация Singleton для подключения к базе данных.
#
# Создайте класс DatabaseConnection, который будет реализовывать паттерн Singleton.
# Этот класс должен содержать информацию о подключении к базе данных и обеспечивать, что существует
# только один экземпляр подключения.
#
# Требования:
# Реализуйте класс DatabaseConnection с атрибутом класса _instance, который будет хранить единственный экземпляр класса.
# Метод __new__ должен гарантировать, что создается только один экземпляр класса.
# Реализуйте метод connect, который будет выводить сообщение о подключении к базе данных.
# Продемонстрируйте, что при создании нескольких объектов класса DatabaseConnection все они ссылаются на
# один и тот же экземпляр.
#
# Задание 2: Реализация Singleton для логгера.
#
# Создайте класс Logger для ведения логов, который будет реализовывать паттерн Singleton.
# Этот класс должен обеспечивать, что существует только один экземпляр логгера.
#
# Требования:
#
# Реализуйте класс Logger с атрибутом класса _instance, который будет хранить единственный экземпляр класса.
# Метод __new__ должен гарантировать, что создается только один экземпляр класса.
# Реализуйте метод log_message, который будет принимать строку и выводить сообщение о записи лога.
# Продемонстрируйте, что при создании нескольких объектов класса Logger все они ссылаются на один и тот же экземпляр.

class DatabaseConnection:
    pass


class Logger:
    pass


def main():
    # Создание объектов подключения к базе данных
    db1 = DatabaseConnection("database_url_1")
    db2 = DatabaseConnection("database_url_2")

    # Проверка, что оба объекта ссылаются на один и тот же экземпляр
    print(db1 is db2)  # Output: True

    # Вызов метода connect
    db1.connect()  # Output: Connecting to the database at database_url_1
    db2.connect()  # Output: Connecting to the database at database_url_1

    # Создание объектов логгера
    logger1 = Logger()
    logger2 = Logger()

    # Проверка, что оба объекта ссылаются на один и тот же экземпляр
    print(logger1 is logger2)  # Output: True

    # Вызов метода log_message
    logger1.log_message("First log message")  # Output: Log: First log message
    logger2.log_message("Second log message")  # Output: Log: Second log message

    # Проверка, что логи сохраняются в одном экземпляре
    print(logger1.logs)  # Output: ['First log message', 'Second log message']
    print(logger2.logs)  # Output: ['First log message', 'Second log message']


if __name__ == "__main__":
    main()

# True
# Connecting to the database at database_url_1
# Connecting to the database at database_url_1
# True
# Log: First log message
# Log: Second log message
# ['First log message', 'Second log message']
# ['First log message', 'Second log message']
