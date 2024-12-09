# Создайте базовый класс человека с именем и возрастом.
# Выведите из него класс студента, с идентификатором и преподавателем.
# Выведите класс преподавателя, который имеет список студентов.
# При добавлении студента в список к преподавателю, этот преподаватель должен устанавливаться в свойстве у студента.
# В список студентов могут быть добавлены ТОЛЬКО студенты, просто человека добавить нельзя.
# Создайте класс работника (Employee) который может вмещать как студентов так и преподавателей и при печати возвращать
# имя и зарплату

from typing import List

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.teacher = None

    def set_teacher(self, teacher):
        self.teacher = teacher

    def __str__(self):
        teacher_name = self.teacher.name if self.teacher else "None"
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}, Teacher: {teacher_name}"

class Teacher(Human):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            student.set_teacher(self)
        else:
            raise ValueError("Можно добавлять только студентов")

    def __str__(self):
        student_list = [str(student) for student in self.students]
        return f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}, Students: {student_list}"

class Employee:
    def __init__(self, human, salary):
        if not isinstance(human, (Student, Teacher)):
            raise ValueError("Employee can only be a Student or a Teacher")
        self.human = human
        self.salary = salary

    @property
    def name(self):
        return self.human.name

    def __str__(self):
        return f"{self.name}, зарплата: {self.salary}"


def main():
    student1 = Student("Alice", 20, "S001")
    student2 = Student("Bob", 22, "S002")
    teacher = Teacher("Mr. Smith", 35, "Math")
    human1 = Human("John", 25)
    #teacher.students = [student1, student2]
    # teacher.students.append(human1) - должен вернуть ошибку!

    teacher.add_student(student1)
    teacher.add_student(student2)


    try:
        teacher.add_student(human1)
    except ValueError as e:
        print(e)


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
