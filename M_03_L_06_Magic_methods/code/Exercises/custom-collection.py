# Создайте класс CustomCollection, который будет поддерживать методы __getitem__, __setitem__ и __delitem__.

class CustomCollection:
    pass


def main():
    # Тестирование
    cc = CustomCollection()
    cc['x'] = 100  # Setting the value for key: x to 100
    cc['y'] = 200  # Setting the value for key: y to 200

    print(cc['x'])  # Getting the value for key: x, Output: 100
    print(cc)  # Output: {'x': 100, 'y': 200}

    del cc['x']  # Deleting the value for key: x
    print(cc)  # Output: {'y': 200}


if __name__ == '__main__':
    main()

# Setting the value for key: x to 100
# Setting the value for key: y to 200
# Getting the value for key: x
# 100
# {'x': 100, 'y': 200}
# Deleting the value for key: x
# {'y': 200}