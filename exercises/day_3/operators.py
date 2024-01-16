"""Day 3: 30 Days of python programming"""

# Declare your age as integer variable
AGE = 40
# Declare your height as a float variable
HEIGHT = 1.85
# Declare a variable that store a complex number
COMPLEX = 4 + 4j
# Write a script that prompts the user to enter base and height of the triangle
#  and calculate an area of this triangle (area = 0.5 x b x h).
#  Enter base: 20
#  Enter height: 10
#  The area of the triangle is 100
triangle_base = input("Enter base: ")
triangle_height = input("Enter height: ")
print("The area of the triangle is ", 0.5 * float(triangle_base) * float(triangle_height))
# Write a script that prompts the user to enter side a, side b, and side c of the triangle.
# Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12
side_a = input("Enter side a: ")
side_b = input("Enter side b: ")
side_c = input("Enter side c: ")
print("The perimeter of the triangle is ", int(side_a) + int(side_b) + int(side_c))
# Get length and width of a rectangle using prompt.
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
rectangle_height = input("Enter height: ")
rectangle_width = input("Enter width: ")
print("The area of the rectangle is ",
      int(rectangle_height) * int(rectangle_width),
      " and the perimeter is ",
      2 * (int(rectangle_height) + int(rectangle_width)))
# Get radius of a circle using prompt.
circle_radius = input("Enter circle radius")
# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
area = 2 * 3.14 * float(circle_radius)


def y_value(x):
    """
    solve the function
    """
    return 2 * x - 2


def slope(x1, x2, y1, y2):
    """
    Calculate the slope
    """
    if x2 - x1 == 0:
        return 0
    else:
        return (y2 - y1) / (x2 - x1)


def euclidean(x, y):
    """
    Calculate the euclidean
    """
    return (abs(y[1] - x[1]) ** 2 + abs(y[0] - x[0]) ** 2) ** -1


X_1 = 0
Y_1 = y_value(X_1)
X_2 = 1
Y_2 = y_value(X_2)
print("Slope is", slope(X_1, X_2, Y_1, Y_2))
print("X-intercept is", Y_1)
print("Y-intercept is", X_2)
# Slope is (m = y2-y1/x2-x1).
# Find the slope and Euclidean distance between point (2, 2) and point (6,10)
print("Slope is ", slope(2, 2, 6, 10))
print("Euclidean is ", euclidean((2, 2), (6, 10)))
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9).
# Try to use different x values and figure out at what x value y is going to be 0.
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print('length of python is', len('python'))
print('length of dragon is', len('dragon'))
print('python and dragon are equal: ', 'python' == 'dragon')
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on in python', 'on' in 'python')
print('on in dragon', 'on' in 'dragon')
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('on in I hope this course is not full of jargon.', 'on' in 'I hope this course is not full of jargon.')
# There is no 'on' in both dragon and python
print('not on in dragon and python', 'on' not in 'dragon' and 'on' not in 'python')
# Find the length of the text python and convert the value to float and convert it to string
print(str(float(len('python'))))
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print("2 is even: ", 2 % 2 == 0)
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print("Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.",
      7//3 == int(2.7))
# Check if type of '10' is equal to type of 10
print("type of '10' is equal to type of 10", type('10') == type(10))
# Check if int('9.8') is equal to 10
print("int('9.8') is equal to 10", int('9.8') == 10)
# Write a script that prompts the user to enter hours and rate per hour.
# Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
hours = input("Enter hours: ")
rate_per_hour = input("Enter rate per hour: ")
print("Your weekly earning is ", int(hours) * int(rate_per_hour))
# Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
years = input('Enter number of years you have lived: ')
print('You have lived for ', years * 365 * 24 * 60 * 60 , ' seconds.')
#     Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
print('1 1 1 1 1')
print('2 1 2 4 8')
print('1 1 1 1 1')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')
