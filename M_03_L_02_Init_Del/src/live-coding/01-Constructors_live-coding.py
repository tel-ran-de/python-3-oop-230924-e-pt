class BaseClass:
    def __init__(self, name):
        self.name = name
        print(f"BaseClass __init__ called for {self.name}")

    def __del__(self):
        print(f"BaseClass __del__ called for {self.name}")


class DerivedClass(BaseClass):
    def __init__(self, name, age):
        """
        Constructor with params
        :param name:
        :param age:
        """
        print(f"DerivedClass __init__ started for {name}")
        super().__init__(name)  # Call BaseClass constructor and send it param "name"
        self.age = age
        print(f"DerivedClass __init__ finished for {self.name}, age {self.age}")

    def __del__(self):
        print(f"DerivedClass __del__ called for {self.name}, age {self.age}")
        super().__del__()


def main():
    # Создание объекта
    print("Creating object...")
    obj = DerivedClass("John", 25)

    # Удаление объекта
    print("Deleting object...")
    del obj


if __name__ == "__main__":
    main()
