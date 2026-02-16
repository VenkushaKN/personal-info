
#\\ -----------------------------
# Welcome Message
# -----------------------------
print("=" * 50)
print("        PERSONAL INFORMATION MANAGER")
print("=" * 50)
print("Welcome to the Personal Information Manager!")
print()

# -----------------------------
# Step 1: Static Information
# -----------------------------

# Store name (string)
name = "Venkusha"

# Store age (integer)
age = 18

# Store city (string)
city = "Madurai"

# Store hobby (string)
hobby = "Listening to music"

# -----------------------------
# Step 2: User Input with Validation
# -----------------------------

print("Please enter your favorite details:")
print("-" * 50)

# Get favorite food with validation
favorite_food = input("Enter your favorite food: ")

while favorite_food.strip() == "":
    print("Error: Input cannot be empty.")
    favorite_food = input("Enter your favorite food: ")

# Get favorite color with validation
favorite_color = input("Enter your favorite color: ")

while favorite_color.strip() == "":
    print("Error: Input cannot be empty.")
    favorite_color = input("Enter your favorite color: ")

# -----------------------------
# Step 3: Calculation
# -----------------------------

# Calculate age in months
age_in_months = age * 12

# -----------------------------
# Step 4: Display Information
# -----------------------------

print()
print("=" * 50)
print("            YOUR INFORMATION")
print("=" * 50)

# Display static information using formatted strings
print(f"Name           : {name}")
print(f"Age            : {age} years")
print(f"Age in Months  : {age_in_months} months")
print(f"City           : {city}")
print(f"Hobby          : {hobby}")

print("-" * 50)

# Display user input information
print(f"Favorite Food  : {favorite_food}")
print(f"Favorite Color : {favorite_color}")

print("=" * 50)

# -----------------------------
# Step 5: Goodbye Message
# -----------------------------

print("Thank you for using the Personal Information Manager!")
print("Program ended successfully.")
print("=" * 50)