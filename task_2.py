class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
             return 'Ошибка'
          
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        

class Lecturer(Mentor):
    def __init__(self, lecturer):
        self.lecturer = lecturer
        self.courses_attached = []
        self.grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

lecturer = Mentor('Some', 'Buddy')
lecturer.courses_attached += ['Python']    

lecturer.rate_lecturer(lecturer, 'Python', 10)
lecturer.rate_lecturer(lecturer, 'Python', 10)
lecturer.rate_lecturer(lecturer, 'Python', 10)

print(lecturer.grades)