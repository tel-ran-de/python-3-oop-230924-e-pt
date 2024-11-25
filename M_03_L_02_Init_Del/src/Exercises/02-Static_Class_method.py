# Задание 1: Работа с методами класса.
# Создайте класс Library, который будет отслеживать количество созданных библиотек и
# хранить общее количество книг во всех библиотеках.
#
# Реализуйте атрибут класса total_books, который будет отслеживать общее количество книг во всех библиотеках.
# Реализуйте метод класса get_total_books, который будет возвращать значение total_books.
# Реализуйте метод класса add_books, который будет принимать количество книг в качестве аргумента и
# добавлять их к total_books.
# Метод __init__ должен увеличивать счетчик количества библиотек.
#
# Задание 2: Работа со статическими методами.
# Создайте класс MathOperations, который будет содержать статические методы для
# выполнения различных математических операций.
#
# Реализуйте статический метод add, который будет принимать два числа и возвращать их сумму.
# Реализуйте статический метод subtract, который будет принимать два числа и возвращать результат их вычитания.
# Реализуйте статический метод multiply, который будет принимать два числа и возвращать их произведение.
# Реализуйте статический метод divide, который будет принимать два числа и возвращать результат их деления.
# Если второе число равно нулю, метод должен возвращать сообщение об ошибке.


class Library:
    pass


class MathOperations:
    pass


def main():
    # Создание объектов библиотеки
    library1 = Library()
    library2 = Library()

    # Добавление книг
    Library.add_books(100)
    Library.add_books(200)

    # Получение общего количества книг
    print(f"Total books in all libraries: {Library.get_total_books()}")  # Output: Total books in all libraries: 300
    print(f"Total number of libraries: {Library.total_libraries}")  # Output: Total number of libraries: 2

    # Вызов статических методов
    print('\n')
    print('* ' * 20)
    print('Вызов статических методов')
    print(f'Method "Add": {MathOperations.add(5, 3)}')  # Output: 8
    print(f'Method "Subtract": {MathOperations.subtract(5, 3)}')  # Output: 2
    print(f'Method "Multiply": {MathOperations.multiply(5, 3)}')  # Output: 15
    print(f'Method "Divide by 0": {MathOperations.divide(5, 0)}')  # Output: Error: Division by zero
    print(f'Method "Divide": {MathOperations.divide(5, 3)}')  # Output: 1.666...


if __name__ == '__main__':
    main()

# Вызов статических методов
# Method "Add": 8
# Method "Subtract": 2
# Method "Multiply": 15
# Method "Divide by 0": Error: Division by zero
# Method "Divide": 1.6666666666666667
