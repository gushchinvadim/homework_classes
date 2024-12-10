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

student_one.courses_in_progress.append("Math")
student_one.courses_in_progress.append("Git")
student_one.courses_in_progress.append("Python")
student_one.finished_courses.append("Введение в программирование")

student_one.grades["Math"] = 8
student_one.grades["Git"] = 9
student_one.grades["Python"] = 10

student_two.courses_in_progress.append("Math")
student_two.courses_in_progress.append("Git")
student_two.grades["Math"] = 8
student_two.grades["Git"] = 9

print(student_one < student_two)


# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
# (в качестве аргументов принимаем список студентов и название курса);


def get_middle_mark_by_course(list_student: [Student], name_course: str) -> float:
    summa_marks = 0
    count_student = 0
    for student in list_student:
        if name_course in student.courses_in_progress:
            summa_marks += student.grades[name_course]
            count_student += 1

    if count_student > 0:
        return summa_marks / count_student
    return 0


middle_mark_math = get_middle_mark_by_course(list_student=[student_one, student_two], name_course="Math")
print(f"Средний балл за математику среди студентов {middle_mark_math}")
middle_mark_initial = get_middle_mark_by_course([student_one, student_two], "Введение в программирование")
print(f"Средний балл за Введение в программирование среди студентов {middle_mark_initial}")
middle_mark_python = get_middle_mark_by_course([student_one, student_two], "Python")
print(f"Средний балл за питон среди студентов {middle_mark_python}")
middle_mark_git = get_middle_mark_by_course([student_one, student_two], "Git")
print(f"Средний балл за гит среди студентов {middle_mark_git}")

# для подсчета средней оценки за лекции всех лекторов в рамках курса
# (в качестве аргумента принимаем список лекторов и название курса).

