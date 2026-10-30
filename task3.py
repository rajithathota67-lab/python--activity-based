# Attendance Percentage Calculator

total_classes = int(input("Enter total number of classes: "))
attended_classes = int(input("Enter attended classes: "))
required_percentage = float(input("Enter required attendance percentage: "))

# Calculate current attendance
current_percentage = (attended_classes / total_classes) * 100

print("Current Attendance Percentage:", round(current_percentage, 2), "%")

# Find minimum classes required
if current_percentage >= required_percentage:
    print("You have already reached the required attendance.")
    print("Minimum additional classes required: 0")
else:
    classes = 0

    while ((attended_classes + classes) /
           (total_classes + classes)) * 100 < required_percentage:
        classes += 1

    print("Minimum consecutive classes to attend:", classes)