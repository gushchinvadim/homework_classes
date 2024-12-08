
grades_student = {'Python': [10,8,5], 'Git': [9, 10, 7]}
rate_lecturer = {'Python': [9,8,5], 'Git': [8, 10, 9]}

value = grades_student.pop('Python')
average = round((sum(value)/len(value)),1)
print(f" Python average student: {average}")

value_2 = grades_student.pop('Git')
average_1 = round((sum(value_2)/len(value_2)),1)
print(f" Git average student: {average_1}")

midle_mark = (round((average + average_1)/2,2))
print(f" Средняя оценка за домашние задания {midle_mark}")

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
    print:('Средние оценки по курсам одинаковые')
