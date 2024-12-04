# класс Countdown создает обратный отсчет

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        current = self.current
        self.current -= 1
        return current


def main():
    # Тестирование
    countdown = Countdown(5)
    for num in countdown:
        print(num)  # Output: 5 4 3 2 1 0


if __name__ == '__main__':
    main()
