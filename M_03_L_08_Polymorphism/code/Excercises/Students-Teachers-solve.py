

from typing import List


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Human):
    def __init__(self, student_id, **kwargs, ):
        super().__init__(**kwargs)
        self.student_id = student_id
        self.teacher = None

    def __str__(self):
        return f"{super().__str__()}, Student ID: {self.student_id}, Teacher: {self.teacher.name}"


class StudentsList(list):
    def append(self, __object):
        if not isinstance(__object, Student):
            raise ValueError("Invalid student type")
        super().append(__object)


class Teacher(Human):
    def __init__(self, subject, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subject = subject
        self.__students = StudentsList()

    @property
    def students(self) -> List[Student]:
        return self.__students

    @students.setter
    def students(self, students: List[Student]):
        for student in students:
            if not isinstance(student, Student):
                raise ValueError("Invalid student type")
            if student not in self.__students:
                self.__students.append(student)
                student.teacher = self

    def __str__(self):
        return (f"{super().__str__()}, Subject: {self.subject}, Students: "
                f"{[student.__str__() for student in self.students]}")


class Employee(Human):
    def __init__(self, human: Human, salary: float = 0.0):
        super(Employee, self).__init__(human.name, human.age)
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    def __str__(self):
        return f"{super(Employee, self).__str__()}, Salary: {self.__salary}"


def main():
    student1 = Student(name="Alice", age=20, student_id="S001")
    student2 = Student(name="Bob", age=22, student_id="S002")
    teacher = Teacher(name="Mr. Smith", age=35, subject="Math")
    teacher.students = [student1, student2]
    # teacher.students.append(Human("John", 25))

    print(student1)
    print(student2)
    print(teacher)

    employees = [Employee(human=student2, salary=10000), Employee(human=teacher, salary=50000)]

    print('Employees:')
    for employee in employees:
        print(employee)


if __name__ == "__main__":
    main()
