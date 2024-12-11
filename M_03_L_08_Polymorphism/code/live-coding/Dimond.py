class A:
    def __init__(self, a):
        self.a = a

        print(f'Initialise A with {a}')

class B(A):
    def __init__(self, b, a):
        super(B, self).__init__(a)
        self.b = b

        print(f'Initialise B with {b}')

class C(A):
    def __init__(self, c, a):
        super(C, self).__init__(a)
        self.c = c

        print(f'Initialise C with {c}')

class D(B, C):
    def __init__(self, d, b, c, a):
        super(D, self).__init__(b, a)
        self.d = d

        print(f'Initialise D with {d}')


def main():
    print(D.__mro__)
    d = D(10, 20, 30, 40)


if  __name__ == '__main__':
    main()
