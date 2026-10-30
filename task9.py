# Inventory Management Using Tuples

products = []

n = int(input("Enter number of products: "))
minimum_stock = int(input("Enter minimum stock level: "))

# Store product details in tuples
for i in range(n):
    print("\nEnter details of Product", i + 1)

    product_id = input("Enter product ID: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter stock quantity: "))

    product = (product_id, price, quantity)
    products.append(product)

# Calculate inventory value
total_value = 0

print("\n----- INVENTORY DETAILS -----")

for product in products:
    product_id, price, quantity = product

    value = price * quantity
    total_value += value

    print("\nProduct ID:", product_id)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Inventory Value:", value)

# Display total inventory value
print("\nTotal Inventory Value:", total_value)

# Identify products needing replenishment
print("\n----- REPLENISHMENT REPORT -----")

found = False

for product in products:
    if product[2] <= minimum_stock:
        print("Product ID:", product[0], "- Replenishment Required")
        found = True

if not found:
    print("No products need replenishment.")