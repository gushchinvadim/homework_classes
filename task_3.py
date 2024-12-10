class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_attached = []
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f" print(some_student) \n "
                f"Имя: {self.name} \n "
                f"Фамилия: {self.surname} \n "
                # f"пол: {self.gender} \n "
                f"Средняя оценка за домашние задания: {self.middle_grade()} \n "
                f"Курсы в процессе изучения: {self.courses_in_progress} \n "
                f"Завершенные курсы: {self.finished_courses}")

    def __lt__(self, other):     
        return self.middle_grade() < other.middle_grade()

    def middle_grade(self) -> float:
        marks = self.grades.values()
        if len(marks) > 0:
            return sum(marks) / len(marks)
        return 0

    def lecturer_rate(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.courses_in_progress = []
        self.rates = {}

    def __str__(self):
        return (f" print(some_lecturer) \n "
                f"Имя: {self.name} \n "
                f"Фамилия: {self.surname}")


class Reviewer(Mentor):
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f" print(some_reviewer) \n "
                f"Имя: {self.name} \n "
                f"Фамилия: {self.surname}")


student_one = Student("Ivan", "Ivanov", "man")
student_two = Student("Michail", "Ivanov", "man")

lecturer_one = Lecturer('Nicola','Tesla')
lecturer_two = Lecturer('Joe','Bidon')

reviewer = Reviewer('Mike','Tyson')

student_one.courses_in_progress.append("Math")
student_one.courses_in_progress.append("Git")
student_one.courses_in_progress.append("Python")
student_one.finished_courses.append("Введение в программирование")

student_one.grades["Math"] = 8
student_one.grades["Git"] = 9
student_one.grades["Python"] = 7

student_two.courses_in_progress.append("Math")
student_two.courses_in_progress.append("Git")
student_two.grades["Math"] = 8
student_two.grades["Git"] = 9

print(lecturer_one)
print(reviewer)
print(student_one)
print(student_one < student_two)