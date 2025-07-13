#list of students and grades on physics class
students_grades = {
        'mamad':20, 'sajjad':18, 'rahman':16, 'jafar':5, 'reza':0
}

#checking pass and fail
for name, grade in students_grades.items():
    if grade >= 10:
        print(f"{name} got {grade} and passed!")
    else:
        print(f"{name} got {grade} and failed!")

