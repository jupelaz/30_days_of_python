"""Day 14: 30 Days of python programming"""
from functools import reduce
from data import countries as more_countries
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Exercises: Level 1
# Explain the difference between map, filter, and reduce.
# Explain the difference between higher order function, closure and decorator
# Define a call function before map, filter or reduce, see examples.
# Use for loop to print each country in the countries list.
_ = [*map(print, countries)]
print(*countries, sep="\n")
# Use for to print each name in the names list.
# Use for to print each number in the numbers list.
# Exercises: Level 2
# Use map to create a new list by changing each country to uppercase in the countries list
new_countries = map(lambda x: x.upper(), countries)
print(*new_countries)
# Use map to create a new list by changing each number to its square in the numbers list
new_numbers = map(lambda x: x ** 2, numbers)
print(*new_numbers)
# Use map to change each name to uppercase in the names list
new_names = map(lambda x: x.upper(), names)
print(*names)
# Use filter to filter out countries containing 'land'.
print(*filter(lambda x: 'land' in x, countries))
# Use filter to filter out countries having exactly six characters.
print(*filter(lambda x: len(x) == 6, countries))
# Use filter to filter out countries containing six letters and more in the country list.
print(*filter(lambda x: len(x) > 6, countries))
# Use filter to filter out countries starting with an 'E'
print(*filter(lambda x: x[0] == 'E', countries))
# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
print(reduce(lambda x, y: x + y, list(filter(lambda x: x % 2 == 0, numbers))))
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.


def get_string_lists(lst: list):
    return list(filter(lambda x: isinstance(x, str), lst))


print(get_string_lists(countries + numbers))
# Use reduce to sum all the numbers in the numbers list.
print(reduce(lambda x, y: x + y, numbers))
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorice_countries(pattern:str):
    return filter(lambda x: pattern in x, more_countries)
# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
# Exercises: Level 3
# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
# Sort countries by name, by capital, by population
# Sort out the ten most spoken languages by location.
# Sort out the ten most populated countries.