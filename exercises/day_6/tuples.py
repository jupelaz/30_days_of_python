"""Day 6: 30 Days of python programming"""

# Exercises: Level 1
# Create an empty tuple
tpl = ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
bros = ("Sergio", "Manolo", "Godofredo")
sis = ("Sergia", "Manola", "Godofreda")
print(bros)
print(sis)
# Join brothers and sisters tuples and assign it to siblings
siblings = bros + sis
print(siblings)
# How many siblings do you have?
print(len(siblings))
# Modify the siblings tuple and add the name of your father,
# and mother and assign it to family_members
family_members = bros + sis + ("Gonzalo", "Espe")
print(family_members)
# Exercises: Level 2
# Unpack siblings and parents from family_members
siblings = family_members[:5]
parents = family_members[5:]
# Create fruits, vegetables and animal products tuples.
fruits = ("apples", "oranges", "bananas")
vegetables = ("tomatoes", "lettuces", "potatoes")
animal_products = ("filet", "burger", "sausages")
# Join the three tuples and assign it to a variable called food_stuff_tp.
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_tp)
print(food_stuff_lt)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
del food_stuff_lt[len(food_stuff_lt)//2]
print(food_stuff_tp)
print(food_stuff_lt)
# Slice out the first three items and the last three items from food_staff_lt list
food_stuff_lt = food_stuff_lt[3:-3]
print(food_stuff_tp)
print(food_stuff_lt)
# Delete the food_staff_tp tuple completely
del food_stuff_tp
print(food_stuff_lt)
# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)
# Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)
