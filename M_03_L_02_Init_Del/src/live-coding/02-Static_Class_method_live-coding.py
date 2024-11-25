class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(Vector.norm2(self.x, self.y))

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def norm2(x, y):
        return x * x + y * y

    def get_coord(self):
        return self.x, self.y


def main():
    v = Vector(10, 20)
    print(v.get_coord())


if __name__ == '__main__':
    main()
