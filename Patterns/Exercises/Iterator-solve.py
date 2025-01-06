# Задача:
#
# Реализуйте паттерн Iterator для обхода коллекции имен студентов.
#
# Шаги:
# Создайте класс коллекции студентов.
# Создайте класс итератора для этой коллекции.
# Реализуйте методы __iter__ и __next__ для итератора.

class StudentCollection:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def __iter__(self):
        return StudentIterator(self.students)


class StudentIterator:
    def __init__(self, students):
        self._students = students
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._students):
            student = self._students[self._index]
            self._index += 1
            return student
        else:
            raise StopIteration


def main():
    # Тестирование
    students = StudentCollection()
    students.add_student("Alice")
    students.add_student("Bob")
    students.add_student("Charlie")

    for student in students:
        print(student)  # Output: Alice Bob Charlie


if __name__ == "__main__":
    main()
