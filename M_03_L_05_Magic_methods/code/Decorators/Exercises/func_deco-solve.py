# Необходимо логировать время вызова каждой функции и значения параметров с которыми она была вызвана
# Необходимо логировать как весь процесс для всей программы, так и вызовы для каждой функции отдельно
# Необходимо предусмотреть возможность дополнительного вывода той же информации в консоль
# Имя файла должно совпадать с именем функции:
# Например для функции main должен быть создан файл с именем main.log

import datetime


# Decorator for main logger
def my_main_logger(file_name: str = None, func_file: bool = False, consol_log: bool = False, *param, **params):
    def decorator_wrapper(func):
        def wrapper(*args, **kwargs):
            # Открываем файл на запись
            if func_file:
                func_file_name = func.__name__ + '.log'
            else:
                func_file_name = file_name

            with open(func_file_name, "w") as file:
                # Дополнительный функционал перед вызовом функции
                file.write(f'{datetime.datetime.now()}, {func.__name__}, {args}, {kwargs}')
                if consol_log:
                    print(f'{datetime.datetime.now()}, {func.__name__}, {args}, {kwargs}')
            # Вызов декорируемой функции с переданными аргументами
            result = func(*args, **kwargs)

            return result
        return wrapper
    return decorator_wrapper


@my_main_logger(file_name='general.log', consol_log=True)
@my_main_logger(func_file=True)
def my_sum(a, b):
    return a + b


@my_main_logger(file_name='general.log', consol_log=True)
@my_main_logger(func_file=True)
def my_sub(a, b):
    return a - b


@my_main_logger(file_name='general.log', consol_log=True)
@my_main_logger(func_file=True)
def my_mul(a, b):
    return a * b


@my_main_logger(file_name='general.log', consol_log=True)
@my_main_logger(func_file=True)
def my_div(a, b):
    return a / b


def main():
    print(my_sum(2, 3))
    print(my_sub(2, 3))
    print(my_mul(2, 3))
    print(my_div(2, 3))


if __name__ == "__main__":
    main()
