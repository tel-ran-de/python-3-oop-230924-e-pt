# Задача:
#
# Реализуйте паттерн Decorator для добавления различных украшений на новогоднюю елку.
# Елка может быть декорирована гирляндами, шарами и звездами.
#
# Шаги:
# Создайте базовый класс для елки.
# Создайте класс декоратора.
# Реализуйте конкретные декораторы для гирлянд, шаров и звезд.

class ChristmasTree:
    def decorate(self):
        return "Christmas tree"


class TreeDecorator(ChristmasTree):
    def __init__(self, tree):
        self._tree = tree

    def decorate(self):
        return self._tree.decorate()


class GarlandDecorator(TreeDecorator):
    def decorate(self):
        return f"{super().decorate()} with Garland"


class BallsDecorator(TreeDecorator):
    def decorate(self):
        return f"{super().decorate()} with Balls"


class StarDecorator(TreeDecorator):
    def decorate(self):
        return f"{super().decorate()} with Star"


def main():
    # Тестирование
    tree = ChristmasTree()
    tree_with_garland = GarlandDecorator(tree)
    tree_with_balls = BallsDecorator(tree_with_garland)
    tree_with_star = StarDecorator(tree_with_balls)

    print(tree_with_star.decorate())  # Output: Christmas tree with Garland with Balls with Star


if __name__ == "__main__":
    main()
