"""Day 9: 30 Days of python programming"""

# Exercises: Level 1
# Get user input using input(“Enter your age: ”).
# If user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years. Output:
#     Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print("You need", 18 - age, "more years to learn to drive.")
# Compare the values of my_age and your_age using if … else.
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age,
# 'years' for bigger differences, and a custom text if my_age = your_age.
# Output:
#     Enter your age: 30
# You are 5 years older than me.
your_age = int(input("Enter your age: "))
MY_AGE = 40
dif = abs(your_age - MY_AGE)
if dif == 1:
    YEARS = "year"
else:
    YEARS = "year"
if your_age > MY_AGE:
    YOUNGER_OLDER = "older"
else:
    YOUNGER_OLDER = "younger"
if dif == 0:
    print("You have the same age than me!")
else:
    print(f'You are {dif} years {YOUNGER_OLDER} than me')
# Get two numbers from the user using input prompt.
# If a is greater than b return a is greater than b,
# if a is less b return a is smaller than b, else a is equal to b.
# Output:
#     Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')
# ### Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
#
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
grade = int(input("Enter your grade: "))
if grade > 100 or grade < 0:
    print("Wrong grade")
    GRADE_ALF = ""
elif grade >= 80:
    GRADE_ALF = "A"
elif grade >= 70:
    GRADE_ALF = "B"
elif grade >= 60:
    GRADE_ALF = "C"
elif grade >= 50:
    GRADE_ALF = "D"
else:
    GRADE_ALF = "F"
# Check if the season is Autumn, Winter, Spring or Summer.
# If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter.
# March, April or May, the season is Spring.
# June, July or August, the season is Summer
month = input("Enter month:")
if month in {"September", "October", "November"}:
    print("The season is Autumn")
elif month in {'December', 'January', 'February'}:
    print("The season is Winter")
elif month in {'March', 'April', 'May'}:
    print("The season is Spring")
elif month in {'June', 'July', 'August'}:
    print("The season is Summer")
# The following list contains some fruits:
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
added_fruit = input("Add a fruit: ")
if added_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(added_fruit)
    print(fruits)
#
# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
#
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# * Check if the person dictionary has skills key,
# if so print out the middle skill in the skills list.
if 'skills' in person:
    print(person['skills'][len(person['skills'])//2])
# * Check if the person dictionary has skills key,
# if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    print("Person has Python skill? ", 'Python' in person['skills'])
# * If a person skills has only JavaScript and React, print('He is a front end developer'),
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
# else print('unknown title') - for more accurate results more conditions can be nested!
if 'JavaStript' in person['skills'] and 'React' in person['skills'] and len(person['skills']) == 2:
    print('He is a front end developer')
elif ('Node' in person['skills'] and 'Python' in person['skills'] and
      'MongoDB' in person['skills'] and len(person['skills']) == 3):
    print('He is a backend developer')
elif ('Node' in person['skills'] and 'React' in person['skills'] and
      'MongoDB' in person['skills']):
    print('He is a fullstack developer')
else:
    print('unknown title')

# * If the person is married and if he lives in Finland,
# print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.
if person['is_marred'] and person['country'] == 'Finland':
    NAME = person["first_name"] + ' ' + person["last_name"]

    print(f'{NAME} lives in {person["country"]}. He is married')
