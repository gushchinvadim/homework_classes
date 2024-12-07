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
        return (f" print(some_student) \n Имя: {self.name} \n Фамилия: {self.surname} \n пол: {self.gender} \n Средняя оценка за домашние задания: {9.9} \n Курсы в процессе изучения: {some_student.courses_in_progress} \n Завершенные курсы: {some_student.finished_courses}") 

    def lecturer_rate(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'
    def __str__(self):
        self.value = value
        if 'Pithon' in self.grades:
             value = self.grades.pop('Pithon')
             print(f" Python average: {(round(sum(value)/len(value)),2)}")
        else:
             value = self.rgades.pop('Git')
             return f" Git average: {(round(sum(value)/len(value)),2)}" 

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
        return (f" print(some_lecturer) \n Имя: {self.name} \n Фамилия: {self.surname}")

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
        return (f" print(some_reviewer) \n Имя: {self.name} \n Фамилия: {self.surname}")   
    
 
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.courses_attached += ['Git']
some_student.courses_attached += ['Pithon']
some_student.finished_courses += ['Введение в программирование']

some_student_1 = Student('Ivan', 'Ivanov', 'male')
some_student_1.courses_in_progress += ['Python']
some_student_1.courses_in_progress += ['Git']
some_student_1.courses_attached += ['Git']
some_student_1.courses_attached += ['Python']
some_student_1.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

some_reviewer_1 = Reviewer('Joe', 'Koker')
some_reviewer_1.courses_attached += ['Python']
some_reviewer_1.courses_attached += ['Git']
 
some_lecturer = Lecturer('Petr', 'Petroff')
some_lecturer.courses_attached += ['Git']
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_in_progress +=['Git']
some_lecturer.courses_in_progress +=['Python']

some_lecturer_1 = Lecturer('Max', 'Linder')
some_lecturer_1.courses_attached += ['Git']
some_lecturer_1.courses_attached += ['Python']
some_lecturer_1.courses_in_progress +=['Git']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 7)

some_reviewer.rate_hw(some_student, 'Git', 8)
some_reviewer.rate_hw(some_student, 'Git', 8)
some_reviewer.rate_hw(some_student, 'Git', 7)

some_reviewer_1.rate_hw(some_student_1, 'Python', 8)
some_reviewer_1.rate_hw(some_student_1, 'Python', 9)
some_reviewer_1.rate_hw(some_student_1, 'Python', 7)

some_reviewer_1.rate_hw(some_student_1, 'Git', 10)
some_reviewer_1.rate_hw(some_student_1, 'Git', 9)
some_reviewer_1.rate_hw(some_student_1, 'Git', 5)

some_student.lecturer_rate(some_lecturer, 'Python', 8)
some_student.lecturer_rate(some_lecturer, 'Git', 10)
some_student.lecturer_rate(some_lecturer, 'Git', 10)
some_student.lecturer_rate(some_lecturer, 'Python', 7)

some_student_1.lecturer_rate(some_lecturer_1, 'Python', 9)
some_student_1.lecturer_rate(some_lecturer_1, 'Python', 9)
some_student_1.lecturer_rate(some_lecturer_1, 'Git', 10)
some_student_1.lecturer_rate(some_lecturer_1, 'Git', 6)


print(some_student.grades)
print(some_student_1.grades)

print(some_lecturer.rates)
print(some_lecturer_1.rates)


rate_lecturer = some_lecturer.rates
rate_lecturer = some_lecturer_1.rates
grades_student = some_student.grades
grades_student = some_student_1.grades


value = grades_student.pop('Python')
average = round((sum(value)/len(value)),1)
print(f" Python average student: {average}")

value_2 = grades_student.pop('Git')
average_1 = round((sum(value_2)/len(value_2)),1)
print(f" Git average student: {average_1}")

value_lecturer = rate_lecturer.pop('Python')
rate = round((sum(value_lecturer)/len(value_lecturer)),1)
print(f" Python rate lecturer: {rate}")

value_lecturer_1 = rate_lecturer.pop('Git')
rate_1 = round((sum(value_lecturer_1)/len(value_lecturer_1)),1)
print(f" Git rate lecturer: {rate_1}")

if average > average_1:
    print("Средняя оценка у студентов курса Python выше чем у курса GIT")
elif average < average_1:
    print("Средняя оценка у студентов курса Git выше чем у курсе Python")      
else:
    print:("Средние оценки по курсам одинаковые")

midle_mark = (round((average + average_1)/2,2))
print(f" Средняя оценка за домашние задания {midle_mark}")