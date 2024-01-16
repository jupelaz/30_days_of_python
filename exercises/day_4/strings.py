"""Day 4: 30 Days of python programming"""

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python'
# to a single string, 'Thirty Days Of Python'.
print(' '.join(['Thirty', 'Days', 'Of', 'Python']))
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print(' '.join(['Coding', 'For' , 'All']))
# Declare a variable named company and assign it to an initial value "Coding For All".
COMPANY = ' '.join(['Coding', 'For' , 'All'])
# Print the variable company using print().
print(COMPANY)
# Print the length of the company string using len() method and print().
print(len(COMPANY))
# Change all the characters to uppercase letters using upper() method.
print(COMPANY.upper())
# Change all the characters to lowercase letters using lower() method.
print(COMPANY.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(COMPANY.capitalize())
print(COMPANY.title())
print(COMPANY.swapcase())
# Cut(slice) out the first word of Coding For All string.
print(COMPANY[1:])
# Check if Coding For All string contains a word Coding
# using the method index, find or other methods.
print('Coding For All string contains a word Coding?',COMPANY.find('Coding') != -1)
# Replace the word coding in the string 'Coding For All' to Python.
print(COMPANY.replace('Coding', 'Python'))
# Change Python for Everyone to Python for All using the replace method or other methods.
print('Python For Everyone'.replace('Everyone', 'All'))
# Split the string 'Coding For All' using space as the separator (split()) .
print('Coding For All'.split())
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))
# What is the character at index 0 in the string Coding For All.
print("the character at index 0 in the string Coding For All is:", "Coding For All"[0])
# What is the last index of the string Coding For All.
print('the last index of the string Coding For All is:', 'Coding For All'[-1])
# What character is at index 10 in "Coding For All" string.
print('character at index 10 in "Coding For All" string is:', "Coding For All"[10])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
print('Python For Everyone'[::2])
# Create an acronym or an abbreviation for the name 'Coding For All'.
print('Coding For All'[::2])
# Use index to determine the position of the first occurrence of C in Coding For All.
print('Coding For All'.index('C'))
# Use index to determine the position of the first occurrence of F in Coding For All.
print('Coding For All'.index('F'))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('Coding For All People'.rfind('l'))
# Use index or find to find the position of the first occurrence
# of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
# Use rindex to find the position of the last occurrence
# of the word because in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))
# Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
SENTENCE = 'You cannot end a sentence with because because because is a conjunction'
RESULT = SENTENCE.replace('because because because', '')
print(RESULT)
# Find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
# Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print(SENTENCE.replace('because because because', ''))
# Does ''Coding For All' start with a substring Coding?
print("'Coding For All".startswith('Coding'))
# Does 'Coding For All' end with a substring coding?
print("'Coding For All".endswith('coding'))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip(' '))
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
# The following list contains the names of some of python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'].
# Join the list with a hash with space string.
print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')
# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')
# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
RADIUS = 10
AREA = 3.14 * RADIUS ** 2
print(f'The area of a circle with radius {RADIUS} is {AREA} meters square.')
# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
X = 8
Y = 6
print(f'{X} + {Y} = {X + Y}')
print(f'{X} - {Y} = {X - Y}')
print(f'{X} * {Y} = {X * Y}')
print(f'{X} / {Y} = {X / Y}')
print(f'{X} % {Y} = {X % Y}')
print(f'{X} // {Y} = {X // Y}')
print(f'{X} ** {Y} = {X ** Y}')
