# Проблема алмаза с передачей параметров в конструкторы.

class A:
    def __init__(self, a):
        # self.value = 42
        print(f"Initializing A with {a}")


class B(A):
    def __init__(self, b, **kwargs):
        super(B, self).__init__(**kwargs)
        self.extra = b
        print(f"Initializing B with {b}")


class C(A):
    def __init__(self, c, **kwargs):
        super(C, self).__init__(**kwargs)
        self.val = c
        print(f"Initializing C with {c}")


class D(B, C):
    def __init__(self, a, b, c, d):
        super(D, self).__init__(a=a, b=b, c=c)
        self.d = d
        print(f"Initializing D with parameters {a, b, c, d}")


def main():
    # Тестирование
    d = D(10, 20, 30, 40)

    # Порядок MRO
    print(D.mro())


if __name__ == "__main__":
    main()
