class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
   
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def disp_name(self):
        print(f" Имя: {self.name}")
        print(f" Фамилия: {self.surname}")

class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    pass

mentor_1 = Reviewer('Иван', 'Иванов') #проверка наследования
mentor_1.disp_name()
