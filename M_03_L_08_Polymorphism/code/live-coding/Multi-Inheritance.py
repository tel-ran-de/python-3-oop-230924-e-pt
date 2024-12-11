# Проблема алмаза с передачей параметров в конструкторы.

class A:
    def __init__(self, a):
        # self.value = 42
        self.a = a
        print(f"Initializing A with {a}")

    def __str__(self):
        return f"A: {self.a}"


class B(A):
    def __init__(self, b, **kwargs):
        super(B, self).__init__(**kwargs)
        self.extra = b
        print(f"Initializing B with {b}")

    def __str__(self):
        return f"B: {self.extra}"


class C(A):
    def __init__(self, c, **kwargs):
        super(C, self).__init__(**kwargs)
        self.val = c
        print(f"Initializing C with {c}")

    def __str__(self):
        return f"C: {self.val}"


class D(B, C):
    def __init__(self, a, b, c, d):
        super(D, self).__init__(a=a, b=b, c=c)
        print(super(D, self).__str__())
        self.d = d
        print(f"Initializing D with parameters {a, b, c, d}")

    def __str__(self):
        return f"D: {self.d}"


def main():
    # Тестирование
    d = D(10, 20, 30, 40)

    # print(d)

    # Порядок MRO
    print(D.mro())


if __name__ == "__main__":
    main()
