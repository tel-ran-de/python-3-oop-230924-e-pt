# Паттерн Composite позволяет сгруппировать объекты в древовидную структуру и
# работать с этими объектами как с единичными объектами.

class Component:
    def operation(self):
        raise NotImplementedError


class Leaf(Component):
    def __init__(self, name):
        self._name = name

    def operation(self):
        return self._name


class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def operation(self):
        results = [child.operation() for child in self._children]
        return f"Composite({', '.join(results)})"


def main():
    leaf1 = Leaf("Leaf1")
    leaf2 = Leaf("Leaf2")

    composite = Composite()
    composite.add(leaf1)
    composite.add(leaf2)

    print(composite.operation())  # Output: Composite(Leaf1, Leaf2)


if __name__ == "__main__":
    main()
