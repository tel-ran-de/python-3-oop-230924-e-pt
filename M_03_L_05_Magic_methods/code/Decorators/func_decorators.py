# Simple decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Дополнительный функционал перед вызовом функции
        print("До вызова функции")
        # Вызов декорируемой функции с переданными аргументами
        result = func(*args, **kwargs)
        # Дополнительный функционал после вызова функции
        print("После вызова функции")
        return result
    return wrapper


# Decorator with parameters
def my_decorator_param(*param, **params):
    def decorator_wrapper(func):
        def wrapper(*args, **kwargs):
            # Дополнительный функционал перед вызовом функции
            print(f"До вызова функции, param: {param}, params: {params}")
            # Вызов декорируемой функции с переданными аргументами
            result = func(*args, **kwargs)
            # Дополнительный функционал после вызова функции
            print(f"После вызова функции param: {param}, params: {params}")
            return result
        return wrapper
    return decorator_wrapper


@my_decorator
def my_function(a, b):
    return a + b


@my_decorator_param("param1", "param2", param3="param3")
def my_function2(a, b):
    return a + b


def main():
    result = my_function(2, 3)
    print(result)
    result = my_function2(2, 3)
    print(result)


if __name__ == "__main__":
    main()
