# Полиморфизм — это концепция объектно-ориентированного программирования (ООП),
# которая позволяет объектам разных классов обрабатывать данные через единый интерфейс.
# Это достигается благодаря тому, что разные классы могут реализовывать методы с одинаковым именем,
# но с различным поведением.
#
# Основные аспекты полиморфизма
# Единый интерфейс: Объекты различных классов могут использоваться через один и тот же интерфейс.
# Переопределение методов: Производные классы могут переопределять методы базового класса,
# предоставляя собственную реализацию.
# Динамическое связывание: Решение о том, какой метод вызывать,
# принимается во время выполнения программы.

# Полиморфизм
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


def make_animal_speak(animal):
    print(animal.speak())


# Полиморфизм через наследование
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


def main():
    print('Polymorphism')
    dog = Dog()
    cat = Cat()

    make_animal_speak(dog)
    make_animal_speak(cat)

    print('Polymorphism with inheritance')
    shapes = [Rectangle(3, 4), Circle(5)]

    for shape in shapes:
        print(shape.area())


if __name__ == "__main__":
    main()
