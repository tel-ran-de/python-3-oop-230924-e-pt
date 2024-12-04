# Паттерн Decorator позволяет динамически добавлять поведение объектам.

class Component:
    def operation(self):
        return "Component"


class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return f"Decorator({self._component.operation()})"


def main():
    component = Component()
    decorated_component = Decorator(component)

    print(decorated_component.operation())  # Output: Decorator(Component)


if __name__ == "__main__":
    main()
