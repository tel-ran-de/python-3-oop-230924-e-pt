from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"

    def move(self):
        return "Running"


class Cat(Animal):
    def speak(self):
        return "Meow!"

    def move(self):
        return "Walking"


def main():
    # Тестирование
    animals = [Dog(), Cat()]

    for animal in animals:
        print(animal.speak())

    # Попытка создания экземпляра абстрактного класса вызывает ошибку
    # animal = Animal()  # Raises TypeError

    print(Animal.__abstractmethods__)


if __name__ == "__main__":
    main()
