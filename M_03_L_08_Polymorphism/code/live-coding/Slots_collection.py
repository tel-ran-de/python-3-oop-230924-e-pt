class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        # self.__length = (x**2 + y**2)**0.5

    @property
    def length(self):
        return (self.x**2 + self.y**2)**0.5


def main():
    p = Point(3, 4)
    print(p.length)


if __name__ == '__main__':
    main()
