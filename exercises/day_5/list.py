"""Day 5: 30 Days of python programming"""

# Declare an empty list
lst = []
# Declare a list with more than 5 items
lst1 = [1,2,3,4,5]
# Find the length of your list
print(len(lst1))
# Get the first item, the middle item and the last item of the list
print(lst1[0],lst1[len(lst1)//2],lst1[-1])
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['juan',40,1.85,'married','capital de euskadi']
# Declare a list variable named it_companies and assign initial values
# Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
print(it_companies[0], it_companies[len(it_companies)//2],it_companies[-1])
# Print the list after modifying one of the companies
it_companies[1] = 'Skype'
print(it_companies)
# Add an IT company to it_companies
it_companies.append('Google')
# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2,'Next')
# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
# Join the it_companies with a string '#;  '
print('#;  '.join(it_companies))
# Check if a certain company exists in the it_companies list.
print(it_companies.count('Google') > 1)
# Sort the list using sort() method
it_companies.sort()
print(it_companies)
# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
# Slice out the first 3 companies from the list
print(it_companies[3:])
# Slice out the last 3 companies from the list
print(it_companies[:-3])
# Slice out the middle IT company or companies from the list
print(it_companies.pop(len(it_companies)//2))
# Remove the first IT company from the list
del it_companies[0]
print(it_companies)
# Remove the middle IT company or companies from the list
del it_companies[len(it_companies)//2]
print(it_companies)
# Remove the last IT company from the list
del it_companies[-1]
print(it_companies)
# Remove all IT companies from the list
del it_companies[:]
print(it_companies)
# Destroy the IT companies list
del it_companies

# Join the following lists:
#
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join = front_end + back_end
# After joining the lists in question 26.
# Copy the joined list and assign it to a variable full_stack.
# Then insert Python and SQL after Redux.
full_stack = join.copy()
full_stack += ["Python", "SQL"]

# Exercises: Level 2
# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
print(ages[0])
print(ages[-1])
# Add the min age and the max age again to the list
MIN_AGE = ages[0]
MAX_AGE = ages[-1]
ages += [MIN_AGE, MAX_AGE]
# Find the median age (one middle item or two middle items divided by two)
ages.sort()
print(ages[len(ages)//2] / 2)
# Find the average age (sum of all items divided by their number )
average = sum(ages)/len(ages)
print(average)
# Find the range of the ages (max minus min)
print(max(ages) - min(ages))
# Compare the value of (min - average) and (max - average), use abs() method
print(max(abs(min(ages) - average), abs(max(ages) - average)))
# Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(countries[len(countries)//2])
# Divide the countries list into two equal lists,
# if it is even if not one more country for the first half.
countries_first = countries[:len(countries)//2]
countries_second = countries[len(countries)//2:]
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].
# Unpack the first three countries and the rest as scandic countries.
first_three = countries[:3]
print(first_three)
scandic = countries[3:]
print(scandic)
