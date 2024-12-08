

# grades = {'Pithon': [10,9,5]}

# values = list(map(str, grades.values()))

# print(values)


# str_1 = 0
# str_1 = ','.join(values)

# print(str_1)


# class Example:
#     def __init__(self):
#         pass
#     def _average(self):
grades = {'Pithon': [10,9,5]}
total_subject_grades = 0
count_subject_grades = 0
for subject, value in grades:
           total_subject_grades += sum(value)
           count_subject_grades += len(value)
print(total_subject_grades / count_subject_grades)




# def overage_grades(self): return sum(self.grades)/len(self.grades)

# total = 0
# for number in str_1:
#         total += number

#         print(total)

# def sum_numbers(numbers, total):
#     total = 0
#     for number in numbers:
#         total += number
#     return total
# sum_numbers([1, 2, 3, 4, 5])
# # 15
# sum_numbers([])
# # 0
# print(total)

# def sum_numbers(numbers):
#     if len(numbers) == 0:
#         return 0
#     return numbers[0] + sum_numbers(numbers[1:])
# sum_numbers([1, 2, 3, 4, 5])