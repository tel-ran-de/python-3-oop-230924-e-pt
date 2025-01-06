# Задача:
#
# Реализуйте паттерн Adapter, чтобы объединить интерфейс нового API системы с устаревшим API.
# Допустим, у вас есть старая система для расчета площади и периметра прямоугольника, и
# вы хотите использовать новую систему, которая использует методы с другими именами и
# принимает данные в другом формате.
#
# Шаги:
# Создайте старую систему с методами для расчета площади и периметра прямоугольника.
# Создайте новую систему с методами, которые используют другой интерфейс.
# Реализуйте адаптер, который преобразует вызовы от старой системы к новой системе.

class OldRectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


class NewRectangle:
    def __init__(self, width, height):
        self.dimensions = (width, height)

    def calculate_area(self):
        return self.dimensions[0] * self.dimensions[1]

    def calculate_perimeter(self):
        return 2 * (self.dimensions[0] + self.dimensions[1])


class RectangleAdapter:
    def __init__(self, new_rectangle):
        self.new_rectangle = new_rectangle

    def get_area(self):
        return self.new_rectangle.calculate_area()

    def get_perimeter(self):
        return self.new_rectangle.calculate_perimeter()


def main():
    # Тестирование
    old_rect = OldRectangle(5, 10)
    print(f"OldRectangle area: {old_rect.get_area()}, perimeter: {old_rect.get_perimeter()}")

    new_rect = NewRectangle(5, 10)
    adapted_rect = RectangleAdapter(new_rect)
    print(f"AdaptedRectangle area: {adapted_rect.get_area()}, perimeter: {adapted_rect.get_perimeter()}")


if __name__ == "__main__":
    main()
