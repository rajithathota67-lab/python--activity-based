# Food Waste Management System

days = int(input("Enter number of days: "))
waste_limit = float(input("Enter waste percentage limit: "))

for i in range(days):
    print("\nEnter details for Day", i + 1)

    prepared = int(input("Enter meals prepared: "))
    served = int(input("Enter meals served: "))

    # Calculate leftover meals
    leftover = prepared - served

    # Calculate waste percentage
    if prepared > 0:
        waste_percentage = (leftover / prepared) * 100
    else:
        waste_percentage = 0

    print("\nDay:", i + 1)
    print("Meals Prepared:", prepared)
    print("Meals Served:", served)
    print("Leftover Meals:", leftover)
    print("Waste Percentage:", round(waste_percentage, 2), "%")

    # Check waste limit
    if waste_percentage > waste_limit:
        print("Alert: Food waste exceeds the limit!")
    else:
        print("Status: Food waste is within the limit.")