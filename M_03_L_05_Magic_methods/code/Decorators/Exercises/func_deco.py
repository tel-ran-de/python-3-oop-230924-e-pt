# Необходимо логировать время вызова каждой функции и значения параметров с которыми она была вызвана
# Необходимо логировать как весь процесс для всей программы, так и вызовы для каждой функции отдельно
# Необходимо предусмотреть возможность дополнительного вывода той же информации в консоль
# Имя файла должно совпадать с именем функции:
# Например для функции main должен быть создан файл с именем main.log

import datetime
now = datetime.datetime.now()


def my_sum(a, b):
    return a + b


def my_sub(a, b):
    return a - b


def my_mul(a, b):
    return a * b


def my_div(a, b):
    return a / b


def main():
    print(my_sum(2, 3))
    print(my_sub(2, 3))
    print(my_mul(2, 3))
    print(my_div(2, 3))


if __name__ == "__main__":
    main()
