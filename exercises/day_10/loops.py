"""Day 10: 30 Days of python programming"""
from data.countries import countries
from data.countries_data import data
print(data)
# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
for NUM in range(11):
    print(NUM)
NUM = 0
while NUM < 11:
    print(NUM)
    NUM += 1
#
# Iterate 10 to 0 using for loop, do the same using while loop.
for NUM in range(10, -1, -1):
    print(NUM)
NUM = 10
while NUM > -1:
    print(NUM)
    NUM -= 1
#
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
# #
# ##
# ###
# ####
# #####
# ######
# #######
for i in range(7):
    print('#' * i)
# Use nested loops to create the following:
#
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
for x in range(8):
    OUTPUT = ''
    for _ in range(8):
        OUTPUT += '# '
    print(OUTPUT)
# Print the following pattern:
#
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for i in range(10):
    print(f'{i} x {i} = {i*i}')
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask']
# using a for loop and print out the items.
for item in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(item)
#
# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0, 101, 2):
    print(i)
#
# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1, 100, 2):
    print(i)
#
# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# print(sum(range(101)))
SUMA = 0
for i in range(101):
    SUMA += i
print(SUMA)
# The sum of all numbers is 5050.
# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
print(sum(range(0, 101, 2)))
print(sum(range(1, 100, 2)))
#
# The sum of all evens is 2550. And the sum of all odds is 2500.
# Exercises: Level 3
# Go to the data folder and use the countries.py file.
# Loop through the countries and extract all the countries containing the word land.

for country in countries:
    if 'land' in country:
        print(country)
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_list = ['banana', 'orange', 'mango', 'lemon']
reversed_fruit_list = []
for fruit in fruit_list:
    reversed_fruit_list.insert(0, fruit)
print(reversed_fruit_list)
# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world

languages = set()
languages_count = {}

for country in data:
    for language in country['languages']:
        languages.add(language)
        if language in languages_count:
            languages_count[language] += 1
        else:
            languages_count[language] = 1
print(len(languages))
languages_count_sorted = sorted(languages_count.items(), key=lambda lang: lang[1])
print(languages_count_sorted[:10])
print(sorted(data, key=lambda country: country['population'], reverse=True)[:10])
