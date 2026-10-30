# Password Validation Program

password = input("Enter your password: ")

errors = []

if len(password) < 8:
    errors.append("Password must contain at least 8 characters.")

if not any(ch.isupper() for ch in password):
    errors.append("Password must contain an uppercase letter.")

if not any(ch.islower() for ch in password):
    errors.append("Password must contain a lowercase letter.")

if not any(ch.isdigit() for ch in password):
    errors.append("Password must contain a digit.")

if not any(not ch.isalnum() for ch in password):
    errors.append("Password must contain a special character.")

# Display results
if len(errors) == 0:
    print("Password is valid!")
else:
    print("Password is invalid.")
    print("Failed Rules:")
    for error in errors:
        print("-", error)