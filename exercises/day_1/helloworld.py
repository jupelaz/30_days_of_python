# Day 1 - 30DaysOfPython Challenge

# Check the python version you are using
import sys
print(sys.version)

# Open the python interactive shell and do the following operations. The operands are 3 and 4.
print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 % 2)             # modulus(%)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 // 2)            # Floor division operator(//)

# Write strings on the python interactive shell. The strings are the following:
print('juan') # Your name
print('pelaz') # Your family name
print('spain') # Your country
print('I am enjoying 30 days of python') # I am enjoying 30 days of python

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

a = (2,3)
b = (10,8)
print(a[0])
print(a[1])

print((((abs(b[1] - a[1]) ** 2) + (abs(b[0] - a[0]) ** 2))) ** -1)