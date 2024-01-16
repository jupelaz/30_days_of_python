"""Day 2: 30 Days of python programming"""
import math

# Exercises: Level 1
first_name = 'joan'  # Declare a first name variable and assign a value to it
last_name = 'pelak'  # Declare a last name variable and assign a value to it
full_name = first_name + last_name # Declare a full name variable and assign a value to it
country = 'spain'  # Declare a country variable and assign a value to it
city = 'logroño'  # Declare a city variable and assign a value to it
age = 40  # Declare an age variable and assign a value to it
year = 2024  # Declare a year variable and assign a value to it
is_married = True  # Declare a variable is_married and assign a value to it
is_true = True  # Declare a variable is_true and assign a value to it
is_light_on = True  # Declare a variable is_light_on and assign a value to it
a, b, c = 0, 1, 2  # Declare multiple variable on one line

# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))
# Using the len() built-in function, find the length of your first name
print(len(first_name))
# Compare the length of your first name and your last name
print(min(first_name, last_name))
print(max(first_name, last_name))
# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
# The radius of a circle is 30 meters.
radius = 30
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 2 * math.pi * (radius ** 2)
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * radius
# Take radius as user input and calculate the area.
new_radius = input("Input user radius")
print(2 * math.pi * (int(new_radius) ** 2))
# Use the built-in input function to get first name, last name, country and age from a user
# and store the value to their corresponding variable names
first_name = input("Insert first name ")
country = input("Insert country ")
age = input("Insert age ")
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
