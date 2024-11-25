# Свойства (Properties)
# Python предоставляет более удобный способ использования геттеров и сеттеров с помощью декоратора property.
# Он позволяет определять геттеры, сеттеры и методы удаления для атрибутов класса в виде свойств.

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
    # Публичные атрибуты
    car = Car(model="Toyota", year=2019)
    print(f'Доступ к публичному атрибуту car.model: {car.model}')  # Доступ к публичному атрибуту
    car.year = 2021  # Изменение публичного атрибута
    print(f'Доступ к публичному атрибуту car.year: {car.year}')  # Output: 2021

    # Приватные атрибуты
    # print(car.__model)  # Ошибка: AttributeError
    print(f'Доступ к приватному атрибуту car.__model: {car.model}')


if __name__ == "__main__":
    main()
