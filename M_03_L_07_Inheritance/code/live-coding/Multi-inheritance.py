class X:
    def __init__(self):
        print("X")


class Y:
    def __init__(self):
        print("Y")


class Z:
    def __init__(self):
        print("Z")


class A(X, Y):
    def __init__(self):
        super().__init__()
        print("A")


class B(Y, Z):
    def __init__(self):
        super().__init__()
        print("B")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("C")


def main():
    # Тестирование
    c = C()
    print(C.__mro__)  # Method Resolution Order


if __name__ == "__main__":
    main()
