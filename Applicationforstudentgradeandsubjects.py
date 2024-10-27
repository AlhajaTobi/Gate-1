students = []
student_grades = []
grades = []


def add_students_and_scores(num_of_students, num_of_subjects):
    for number in range(1, num_of_students+1):
        student = str(input(f"Enter the name of student no:{number}: "))
        students.append(student)
        for subject_number in range(1, num_of_subjects+1):
            score = int(input(f"Enter score for subject({subject_number}): "))
            student_grades.append(score)
        grades.append(student_grades.copy())
        student_grades.clear()
    print(students)
    print(grades)


def calculate_score_total():
    for index in range(len(students)):
        total = 0
        for grade in grades[index]:
            total += grade
        grades[index].append(total)
    print(students)
    print(grades)
    

def calculate_score_average(num_of_subjects):
    avg = 0
    for index in range(len(students)):
        avg = grades[index][num_of_subjects-1]/num_of_subjects
        grades[index].append(avg)
    print(students)
    print(grades)