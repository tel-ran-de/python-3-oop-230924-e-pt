# Создайте класс CustomCollection, который будет поддерживать методы __getitem__, __setitem__ и __delitem__.

class CustomCollection:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        print(f"Getting the value for key: {key}")
        return self.data[key]

    def __setitem__(self, key, value):
        print(f"Setting the value for key: {key} to {value}")
        self.data[key] = value

    def __delitem__(self, key):
        print(f"Deleting the value for key: {key}")
        del self.data[key]

    def __repr__(self):
        return repr(self.data)


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
