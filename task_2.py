class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_attached = []
        # self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
      

    def lectorer_rate(self, lectorer, course, rate):
        if isinstance(lectorer, Lecturer) and course in lectorer.courses_attached:
            if course in lectorer.rates:
                lectorer.rates[course] += [rate]
            else:
                lectorer.rates[course] = [rate]
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

class Reviewer(Mentor):
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_attached += ['Git']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
 
some_lectorer = Lecturer('Some', 'Buddy')
some_lectorer.courses_attached += ['Git']
some_lectorer.courses_in_progress +=['Git']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 5)

some_student.lectorer_rate(some_lectorer, 'Git', 8)
some_student.lectorer_rate(some_lectorer, 'Git', 10)
some_student.lectorer_rate(some_lectorer, 'Git', 7)

print(some_student.grades)

print(some_lectorer.rates)
