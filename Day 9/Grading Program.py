student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for scores in student_scores:
    if student_scores[scores] >= 91:
        student_grades[scores] = "Outstanding"
    elif student_scores[scores] >= 81:
        student_grades[scores] = "Exceeds Expectations"
    elif student_scores[scores] >= 71:
        student_grades[scores] = "Acceptable"
    else:
        student_grades[scores] = "Fail"

# student_grades = student_scores
 
# 🚨 Don't change the code below 👇
print(student_grades)





