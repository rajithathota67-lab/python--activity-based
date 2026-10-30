# Student Performance Analysis

n = int(input("Enter number of subjects: "))

for i in range(n):
    print("\nEnter marks for Subject", i + 1)

    subject = input("Enter subject name: ")
    test1 = float(input("Enter Assessment 1 marks: "))
    test2 = float(input("Enter Assessment 2 marks: "))
    test3 = float(input("Enter Assessment 3 marks: "))

    # Calculate changes
    change1 = test2 - test1
    change2 = test3 - test2

    print("\nSubject:", subject)
    print("Assessment 1:", test1)
    print("Assessment 2:", test2)
    print("Assessment 3:", test3)
    print("Change from Assessment 1 to 2:", change1)
    print("Change from Assessment 2 to 3:", change2)

    # Identify declining performance
    if change1 < 0 or change2 < 0:
        print("Performance: Declining")
    else:
        print("Performance: Not Declining")