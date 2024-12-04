# Создайте класс ComplexNumber, который будет представлять комплексные числа.
# Перегрузите различные магические методы для выполнения арифметических операций, сравнения и для
# управления атрибутами воспользуйтесь методами установки атрибутов.
# Добавьте логирование времени исполнения операций хеширования с помощью класс декоратора TimeLogger


# Классы-декораторы
class TimeLogger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        import time
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {self.func.__name__} executed in {end_time - start_time:.6f} seconds")
        return result


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Арифметические операции
    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real, imag)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            denom = other.real**2 + other.imag**2
            real = (self.real * other.real + self.imag * other.imag) / denom
            imag = (self.imag * other.real - self.real * other.imag) / denom
            return ComplexNumber(real, imag)
        return NotImplemented

    # Сравнения
    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imag == other.imag
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, ComplexNumber):
            return (self.real**2 + self.imag**2) < (other.real**2 + other.imag**2)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, ComplexNumber):
            return (self.real**2 + self.imag**2) <= (other.real**2 + other.imag**2)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, ComplexNumber):
            return (self.real**2 + self.imag**2) > (other.real**2 + other.imag**2)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, ComplexNumber):
            return (self.real**2 + self.imag**2) >= (other.real**2 + other.imag**2)
        return NotImplemented

    # Хеширование
    @TimeLogger
    def __hash__(self):
        return hash((self.real, self.imag))

    # Управление атрибутами
    def __setattr__(self, name, value):
        print(f"Setting attribute {name} to {value}")
        super().__setattr__(name, value)

    def __getattribute__(self, name):
        print(f"Getting attribute {name}")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print(f"Attribute {name} not found, returning default value")
        return "Default value"

    def __delattr__(self, name):
        print(f"Deleting attribute {name}")
        super().__delattr__(name)

    # Вызов объекта
    def __call__(self):
        print(f"ComplexNumber called with ({self.real} + {self.imag}i)")

    # Представление объекта
    def __str__(self):
        return f"({self.real} + {self.imag}i)"

    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imag})"

    # Длина и абсолютное значение
    def __len__(self):
        return 2

    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5



def main():
    # Тестирование
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)
    c3 = ComplexNumber(1, 2)

    # Арифметические операции
    print(c1 + c2)  # Output: (4 + 6i)
    print(c1 - c2)  # Output: (-2 + -2i)
    print(c1 * c2)  # Output: (-5 + 10i)
    print(c1 / c2)  # Output: (0.44 + 0.08i)

    # Сравнения
    print(c1 == c3)  # Output: True
    print(c1 != c2)  # Output: True
    print(c1 < c2)  # Output: True
    print(c1 <= c3)  # Output: True
    print(c1 > c2)  # Output: False
    print(c1 >= c3)  # Output: True

    # Хеширование и использование в set
    complex_set = {c1, c2, c3}
    print(complex_set)  # Output: {ComplexNumber(1, 2), ComplexNumber(3, 4)}

    # Управление атрибутами
    c1.new_attr = 10  # Setting attribute new_attr to 10
    print(c1.new_attr)  # Getting attribute new_attr
    del c1.new_attr  # Deleting attribute new_attr

    # Вызов объекта
    c1()  # Output: ComplexNumber called with (1 + 2i)

    # Представление объекта
    print(str(c1))  # Output: (1 + 2i)
    print(repr(c1))  # Output: ComplexNumber(1, 2)

    # Длина и абсолютное значение
    print(len(c1))  # Output: 2
    print(abs(c1))  # Output: 2.23606797749979


if __name__ == "__main__":
    main()
