class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Person):
            return self.age <= other.age
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Person):
            return self.age >= other.age
        return NotImplemented

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"


def main():
    # Тестирование
    p1 = Person("Alice", 30)
    p2 = Person("Bob", 25)
    p3 = Person("Alice", 30)

    print(p1 == p3)  # Output: True
    print(p1 != p2)  # Output: True
    print(p1 < p2)  # Output: False
    print(p1 <= p3)  # Output: True
    print(p1 > p2)  # Output: True
    print(p1 >= p3)  # Output: True


if __name__ == "__main__":
    main()
