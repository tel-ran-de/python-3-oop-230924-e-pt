# в Python атрибуты класса и объекта могут быть публичными или приватными.
# Публичные атрибуты доступны из любого места в коде,
# тогда как приватные атрибуты скрыты от прямого доступа извне и предназначены для внутреннего использования в классе.
#
# Публичные атрибуты
# Публичные атрибуты — это атрибуты, которые могут быть доступны и изменены извне класса.
# В Python такие атрибуты обозначаются обычным именем без подчеркиваний.

# Приватные атрибуты — это атрибуты,
# которые предназначены для внутреннего использования внутри класса и
# недоступны для прямого доступа извне.
# В Python такие атрибуты обозначаются начальным двойным подчеркиванием (__).

# Геттеры и сеттеры — это методы, которые используются для доступа и управления
# приватными атрибутами объекта.
# Они обеспечивают контроль над доступом к данным,
# позволяя добавлять логику проверки и обработки данных при их получении или изменении.
#
# Геттеры — это методы, которые возвращают значение приватного атрибута.
# Они позволяют получить значение атрибута, не обращаясь к нему напрямую.
# Геттеры обычно именуются с префиксом get.
#
# Сеттеры — это методы, которые устанавливают значение приватного атрибута.
# Они позволяют изменить значение атрибута,
# добавляя при этом логику проверки или обработки данных.
# Сеттеры обычно именуются с префиксом set.
#
# Публичные атрибуты
class Car:
    def __init__(self, model, year, private_model, private_year):
        self.model = model  # Публичный атрибут
        self.year = year    # Публичный атрибут
        self.__private_model = private_model
        self.__private_year = private_year

    def get_private_model(self):
        return self.__private_model

    def set_private_model(self, private_model):
        if isinstance(private_model, str):
            self.__private_model = private_model
        else:
            raise ValueError("Model must be a string")

    def get_private_year(self):
        return self.__private_year

    def set_year(self, private_year):
        if private_year > 1885:  # Первый автомобиль был создан в 1886 году
            self.__private_year = private_year
        else:
            raise ValueError("Year must be greater than 1885")


def main():
    # Публичные атрибуты
    car = Car(model="Toyota", year=2019, private_model="Tesla", private_year=2020)
    print(f'Доступ к публичному атрибуту car.model: {car.model}')  # Доступ к публичному атрибуту
    car.year = 2021  # Изменение публичного атрибута
    print(f'Доступ к публичному атрибуту car.year: {car.year}')  # Output: 2021

    # Приватные атрибуты
    # print(car.__model)  # Ошибка: AttributeError
    print(f'Доступ к приватному атрибуту car.__private_model: {car.get_private_model()}')  # Правильный доступ через метод

    # Установка приватного атрибута
    print('Установка приватного атрибута car.__private_model = "BMW"')
    car.set_private_model("BMW")
    print(f'Доступ к приватному атрибуту car.__private_model: {car.get_private_model()}')


if __name__ == "__main__":
    main()
