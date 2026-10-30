# Student Marks Analysis Using Nested Lists

students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

marks = []

# Read student marks
for i in range(students):
    student_marks = []
    print("\nEnter marks for Student", i + 1)

    for j in range(subjects):
        mark = float(input("Enter marks for Subject " + str(j + 1) + ": "))
        student_marks.append(mark)

    marks.append(student_marks)

# Calculate student total and average
print("\n----- STUDENT RESULTS -----")

for i in range(students):
    total = sum(marks[i])
    average = total / subjects

    print("\nStudent", i + 1)
    print("Marks:", marks[i])
    print("Total:", total)
    print("Average:", round(average, 2))

# Calculate subject averages
print("\n----- SUBJECT AVERAGES -----")

for j in range(subjects):
    total = 0

    for i in range(students):
        total += marks[i][j]

    average = total / students
    print("Subject", j + 1, "Average:", round(average, 2))