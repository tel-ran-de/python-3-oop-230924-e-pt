# Создайте базовый класс человека с именем и возрастом.
# Выведите из него класс студента, с идентификатором и преподавателем.
# Выведите класс преподавателя, который имеет список студентов.
# При добавлении студента в список к преподавателю, этот преподаватель должен устанавливаться в свойстве у студента.
# В список студентов могут быть добавлены ТОЛЬКО студенты, просто человека добавить нельзя.
# Создайте класс работника (Employee) который может вмещать как студентов так и преподавателей и при печати возвращать
# имя и зарплату

from typing import List


class Human:
    pass


class Student(Human):
    pass


class Teacher(Human):
    pass


class Employee(Human):
    pass


def main():
    student1 = Student("Alice", 20, "S001")
    student2 = Student("Bob", 22, "S002")
    teacher = Teacher("Mr. Smith", 35, "Math")
    human1 = Human("John", 25)
    teacher.students = [student1, student2]
    # teacher.students.append(human1) - должен вернуть ошибку!

    print(student1)
    print(student2)
    print(teacher)

    employees = [Employee(human=student2, salary=10000), Employee(human=teacher, salary=50000)]

    print('Employees:')
    for employee in employees:
        print(employee.name, employee.salary)


if __name__ == "__main__":
    main()

# Name: Alice, Age: 20, Student ID: S001, Teacher: Mr. Smith
# Name: Bob, Age: 22, Student ID: S002, Teacher: Mr. Smith
# Name: Mr. Smith, Age: 35, Subject: Math, Students: ['Name: Alice, Age: 20, Student ID: S001, Teacher: Mr. Smith', 'Name: Bob, Age: 22, Student ID: S002, Teacher: Mr. Smith']
# Employees:
# Bob 10000
# Mr. Smith 50000
