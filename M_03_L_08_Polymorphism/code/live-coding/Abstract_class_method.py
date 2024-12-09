from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


def main():
    # Тестирование
    animals = [Dog(), Cat()]

    for animal in animals:
        print(animal.speak())

    # Попытка создания экземпляра абстрактного класса вызывает ошибку
    # animal = Animal()  # Raises TypeError
