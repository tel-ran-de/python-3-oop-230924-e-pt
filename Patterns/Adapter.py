# Паттерн Adapter позволяет объектам с несовместимыми интерфейсами работать вместе.

class OldSystem:
    def old_method(self):
        return "Old System"


class NewSystem:
    def new_method(self):
        return "New System"


class Adapter(NewSystem):
    def __init__(self, old_system):
        self.old_system = old_system

    def new_method(self):
        return f"{self.old_system.old_method()} adapted to {super().new_method()}"


def main():
    old_system = OldSystem()
    adapter = Adapter(old_system)

    print(adapter.new_method())  # Output: Old System adapted to New System


if __name__ == "__main__":
    main()
