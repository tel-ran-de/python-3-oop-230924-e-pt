
class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # def __getattribute__(self, item):
    #     print("__getattribute__")
    #     return object.__getattribute__(self, item)
    #
    def __setattr__(self, key, value):
        print(f"__setattr__ {key} = {value}")
        object.__setattr__(self, key, value)

    # Prohibit changing the private attribute
    def __getattribute__(self, item):
        if item == "_Point__x":
            raise ValueError("Private attribute")
        else:
            return object.__getattribute__(self, item)

    # def __setattr__(self, key, value):
    #     if key == "__x":
    #         raise ValueError("Private attribute")
    #     else:
    #         object.__setattr__(self, key, value)


def main():
    pt = Point(1, 2)
    print(f'pt._Point__x = {pt._Point__x}')
    pt._Point__x = 10
    # print(f'pt._Point__x = {pt._Point__x}')


if __name__ == "__main__":
    main()
