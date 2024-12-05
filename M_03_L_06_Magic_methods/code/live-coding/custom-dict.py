class CustomDict:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __repr__(self):
        return repr(self.data)


class CustomList:
    def __init__(self):
        self.data = []
        self.add_data = []

    def __getitem__(self, index):
        return self.data[index], self.add_data[index]

    def __setitem__(self, index, value1, value2):
        self.data[index] = value1
        self.add_data[index] = value2

    def __delitem__(self, index):
        del self.data[index],  self.add_data[index]

    def __repr__(self):
        return repr(self.data), repr(self.add_data)


def main():
    # Тестирование
    cd = CustomDict()
    cd['a'] = 10  # Установка значения
    cd['b'] = 20
    print(cd)  # Output: {'a': 10, 'b': 20}

    print(cd['a'])  # Получение значения, Output: 10

    del cd['a']  # Удаление значения
    print(cd)  # Output: {'b': 20}


if __name__ == '__main__':
    main()
