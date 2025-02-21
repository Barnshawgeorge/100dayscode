student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if(student_scores[key] >= 91 and student_scores[key] <= 100):
        student_grades[key] = "outstanding"
    if(student_scores[key] <= 90 and student_scores[key] >= 81):
        student_grades[key] = "exceeds"   


print(student_grades)
print(student_scores)

