# Centered Numeric Pyramid

rows = int(input("Enter number of rows: "))

if rows <= 0:
    print("Invalid input! Enter a positive number of rows.")
else:
    for i in range(1, rows + 1):

        # Print spaces
        for j in range(rows - i):
            print(" ", end=" ")

        # Print numbers
        for j in range(1, i + 1):
            print(j, end=" ")

        print()