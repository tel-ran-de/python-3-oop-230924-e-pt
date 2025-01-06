# Задача:
#
# Реализуйте паттерн Composite, чтобы создать структуру, представляющую меню ресторана,
# где каждая категория меню может содержать подкатегории или отдельные элементы.
#
# Шаги:
# Создайте класс компонента, который будет основой для всех частей меню.
# Создайте классы для элементов меню и категорий меню.
# Реализуйте метод для отображения структуры меню.

class MenuComponent:
    def add(self, component):
        pass

    def remove(self, component):
        pass

    def display(self, depth):
        pass


class MenuItem(MenuComponent):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self, depth):
        print(" " * depth + f"Item: {self.name}, Price: {self.price}")


class MenuCategory(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.components = []

    def add(self, component):
        self.components.append(component)

    def remove(self, component):
        self.components.remove(component)

    def display(self, depth=0):
        print(" " * depth + f"Category: {self.name}")
        for component in self.components:
            component.display(depth + 2)


def main():
    # Тестирование
    main_menu = MenuCategory("Main Menu")
    drinks = MenuCategory("Drinks")
    food = MenuCategory("Food")

    coffee = MenuItem("Coffee", 2.50)
    tea = MenuItem("Tea", 1.50)
    sandwich = MenuItem("Sandwich", 5.00)
    salad = MenuItem("Salad", 4.00)

    drinks.add(coffee)
    drinks.add(tea)
    food.add(sandwich)
    food.add(salad)

    main_menu.add(drinks)
    main_menu.add(food)

    main_menu.display()


if __name__ == "__main__":
    main()
