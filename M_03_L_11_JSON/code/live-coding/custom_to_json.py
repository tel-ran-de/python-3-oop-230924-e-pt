import json


class myclass:

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return f"{self.name} {self.age} {self.score}"

    def __str__(self):
        # return f"{self.name} {self.age} {self.score}"
        return str([(key, value) for (key, value) in self.__dict__().items()])

    def __dict__(self):
        return {"name": self.name, "age": self.age, "score": self.score}


def main():
    obj = myclass("John", 30, 100)
    print(obj)
    print(type(obj.__dict__()), obj.__dict__())
    print(type(json.dumps(obj.__dict__())), json.dumps(obj.__dict__()))
    print(obj.__repr__())


if __name__ == '__main__':
    main()
