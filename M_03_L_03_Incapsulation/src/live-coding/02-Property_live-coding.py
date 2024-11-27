class Car:
    def __init__(self, model, year):
        self.__model = model  # Приватный атрибут
        self.__year = year    # Приватный атрибут

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if isinstance(model, str):
            self.__model = model
        else:
            raise ValueError("Model must be a string")

    @model.deleter
    def model(self):
        print("Deleting model...")
        del self.__model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year > 1885:
            self.__year = year
        else:
            raise ValueError("Year must be greater than 1885")


def main():
    car = Car("Toyota", 2020)
    print(car.model)  # Доступ через геттер
    car.year = 2021  # Изменение через сеттер
    print(car.year)


if __name__ == "__main__":
    main()
