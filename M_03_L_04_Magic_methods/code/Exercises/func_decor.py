# Задача: Создание класса-декоратора для времени выполнения функции
# Описание:
#
# Создайте класс-декоратор TimeLogger, который будет логировать время выполнения оборачиваемой функции.
# Класс должен использовать метод __call__ для измерения времени выполнения функции и вывода этой информации на экран.
#
# Требования:
#
# Класс TimeLogger должен принимать функцию в своем конструкторе.
# Метод __call__ должен измерять время выполнения функции и выводить эту информацию на экран.
# Напишите тестовый код, который демонстрирует использование этого декоратора.
import time

# your code here
class TimeLogger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        result_time = end_time - start_time
        print(f"Function {self.func.__name__} executed in {result_time:.8f} seconds")
        return result



def main():
    @TimeLogger
    def slow_function(seconds):
        time.sleep(seconds)
        return f"Function ran for {seconds} seconds"

    @TimeLogger
    def add(a, b):
        time.sleep(0.2)
        return a + b

    # Тестирование декоратора
    print(slow_function(2))  # Output: Function slow_function executed in 2.000... seconds
    print(add(3, 5))  # Output: Function add executed in 0.000... seconds

# Вывод:
# Function slow_function executed in 2.003796 seconds
# Function ran for 2 seconds
# Function add executed in 0.000003 seconds
# 8

if __name__ == '__main__':
    main()
