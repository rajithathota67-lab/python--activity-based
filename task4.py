# Stock Management System

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nEnter details of Product", i + 1)

    name = input("Enter product name: ")
    opening = int(input("Enter opening stock: "))
    incoming = int(input("Enter incoming stock: "))
    dispatched = int(input("Enter dispatched stock: "))
    physical = int(input("Enter physically counted stock: "))

    # Calculate expected closing stock
    expected = opening + incoming - dispatched

    # Calculate discrepancy
    difference = physical - expected

    print("\nProduct Name:", name)
    print("Expected Closing Stock:", expected)
    print("Physical Stock:", physical)

    if difference == 0:
        print("Status: No Discrepancy")
    elif difference > 0:
        print("Status: Excess Stock")
        print("Excess Quantity:", difference)
    else:
        print("Status: Shortage Stock")
        print("Shortage Quantity:", abs(difference))