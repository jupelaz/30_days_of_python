"""Day 13: 30 Days of python programming"""


# Filter only negative and zero in the list using list comprehension
#
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [i for i in numbers if i <= 0]
print(filtered)
# Flatten the following list of lists of lists to a one dimensional list :
#
# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
#
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lst = [sub3 for sub2 in list_of_lists for sub1 in sub2 for sub3 in sub1]
print(lst)

# Using list comprehension create the following list of tuples:
#
# [(0, 1, 0, 0, 0, 0, 0),
#  (1, 1, 1, 1, 1, 1, 1),
#  (2, 1, 2, 4, 8, 16, 32),
#  (3, 1, 3, 9, 27, 81, 243),
#  (4, 1, 4, 16, 64, 256, 1024),
#  (5, 1, 5, 25, 125, 625, 3125),
#  (6, 1, 6, 36, 216, 1296, 7776),
#  (7, 1, 7, 49, 343, 2401, 16807),
#  (8, 1, 8, 64, 512, 4096, 32768),
#  (9, 1, 9, 81, 729, 6561, 59049),
#  (10, 1, 10, 100, 1000, 10000, 100000)]
list_of_tuples = [tuple([i] + [i ** j for j in range(7)]) for i in range(11)]

print(list_of_tuples)
# Flatten the following list to a new list:
#
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country, country[:3].upper(), city[1]] for sub in countries for country, city in sub]
print(output)
# Change the following list to a list of dictionaries:
#
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
#  {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#  {'country': 'NORWAY', 'city': 'OSLO'}]
output_dict_list = [({'country': country.upper(), 'city': city.upper()}) for sub in countries for country, city in sub]
print(output_dict_list)
# Change the following list of lists to a list of concatenated strings:
#
# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [f'{name} {last_name}' for sub in names for name, last_name in sub]
print(output)
# Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda a, b: ((a[0] - b[0]) * (a[1] - b[1])) ** -1
