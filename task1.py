marks = float(input("Enter aggregate marks: "))
minimum_marks = float(input("Enter minimum required marks: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter annual family income: "))

if (marks >= minimum_marks and
    attendance >= 75 and
    income <= 250000):

    print("Congratulations! You are eligible for the scholarship.")
else:
    print("Sorry! You are not eligible for the scholarship.")
