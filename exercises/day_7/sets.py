"""Day 7: 30 Days of python programming"""

# # sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Exercises: Level 1
# Find the length of the set it_companies
print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add("Twitter")
# Insert multiple IT companies at once to the set it_companies
it_companies.update(["Skype", "Next"])
# Remove one of the companies from the set it_companies
it_companies.pop()
# What is the difference between remove and discard? Discard method does not raise errors
# Exercises: Level 2
# Join A and B
A_join_B = A.union(B)
print(A_join_B)
# Find A intersection B
A_intersection_B = A.intersection(B)
print(A_intersection_B)
# Is A subset of B
print(A.issubset(B))
# Are A and B disjoint sets
print(A.isdisjoint(B))
# Join A with B and B with A
A_join_B = A.union(B)
print(A_join_B)
B_join_A = B.union(A)
# What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# Delete the sets completely
del it_companies
del A
del B
# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_set = set(age)
print(f'{len(age)} and {len(ages_set)}')
# Explain the difference between the following data types: string, list, tuple and set
# String is an iterable of characters, list is an ordered mutable collection,
# tuple is an ordered immutable collection, and a set is an unordered collection
# I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence?
# Use the split methods and set to get the unique words.
print(len(set("I am a teacher and I love to inspire and teach people".split(" "))))
