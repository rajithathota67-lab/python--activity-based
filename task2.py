# Simple Bill Calculation

p1 = float(input("Enter price of Product 1: "))
p2 = float(input("Enter price of Product 2: "))
p3 = float(input("Enter price of Product 3: "))

q1 = int(input("Enter quantity of Product 1: "))
q2 = int(input("Enter quantity of Product 2: "))
q3 = int(input("Enter quantity of Product 3: "))

# Calculate subtotal
subtotal = (p1 * q1) + (p2 * q2) + (p3 * q3)

# Apply discount
if subtotal >= 1000:
    discount = subtotal * 0.10
else:
    discount = 0

# Calculate tax
amount = subtotal - discount
tax = amount * 0.05

# Final bill
final_amount = amount + tax

print("\n----- FINAL BILL -----")
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Tax:", tax)
print("Final Amount:", round(final_amount, 2))