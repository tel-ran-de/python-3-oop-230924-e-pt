# Необходимо логировать время вызова каждой функции и значения параметров с которыми она была вызвана
# Необходимо логировать весь процесс для всей программы так и вызовы для каждой функции отдельно
# Имя файла должно совпадать с именем функции:
# Например для функции main должен быть создан файл с именем main.log

import datetime
import time
from pickle import FALSE

from django.db.models.expressions import result
from django.db.models.functions import TruncSecond


def log_function_param(file_name:str=None, wreit_glob:bool=False, wreit_consol:bool=False):

    def log_function(func):
        def wrapper(*args, **kwargs):
            if wreit_glob:
                with open(file_name, "a") as file:
                    file.write(f"{datetime.datetime.now()}, {func.__name__}")
            else:


                log_filename = (f"{func.__name__}.log")
                with open(log_filename, "a") as log_file:
                    log_file.write(f"{datetime.datetime.now()}, {func.__name__}")
            if wreit_consol:
                print(datetime.datetime.now())
            result = func(*args, **kwargs)
            return result
        return wrapper
    return log_function
@log_function_param("global_file.log", True, True)
@log_function_param("global_file.log", False, True)
def my_function2(a, b):
    return a + b

@log_function_param("global_file.log", True, True)
@log_function_param(wreit_glob=False)
def my_sum(a, b):
    return a + b

@log_function_param("global_file.log", True, True)
@log_function_param(wreit_glob=False)
def my_sub(a, b):
    return a - b

@log_function_param("global_file.log", True, True)
@log_function_param(wreit_glob=False)
def my_mul(a, b):
    return a * b

@log_function_param("global_file.log", True, True)
@log_function_param(wreit_glob=False)
def my_div(a, b):
    return a / b


def main():
    print(my_sum(5, 3))
    print(my_sub(2, 3))
    print(my_mul(2, 3))
    print(my_div(10, 3))


if __name__ == "__main__":
    main()
