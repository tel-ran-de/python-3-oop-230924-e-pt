# класс Countdown создает обратный отсчет

class Countdown:
    def __init__(self, start, step, end):
        self.current = end
        self.end = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            raise StopIteration
        current = self.current
        self.current -= self.step
        return current


def main():
    # Тестирование
    countdown = Countdown(-10, 2, 5)
    for num in countdown:
        print(num)  # Output: 5 4 3 2 1 0


if __name__ == '__main__':
    main()
