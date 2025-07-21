programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


def grade_student(score):
    grade = ''
    if score >= 91 and score <= 100:
        grade = "Outstanding"
    elif score >= 81 and score <= 90:
        grade = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        grade = "Acceptable"
    elif score <= 70:
        grade = "Fail"

    return grade

student_grades = {}

for student in student_scores:
    student_grades[student] = grade_student(student_scores[student])

print(student_grades)
