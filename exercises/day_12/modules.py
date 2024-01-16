"""Day 12: 30 Days of python programming"""
import random
import string


# Write a function which generates a six digit/character random_user_id.
# print(random_user_id());
# '1ee33d'
def random_user_id():
    # ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return x


print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user.
# It does not take any parameters, but it takes two inputs using input().
# One of the inputs is the number of characters,
# and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf
#
# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr


def user_id_gen_by_user():
    number_of_characters = int(input('Insert number of characters:'))
    number_of_id = int(input('Insert number of IDs:'))
    for _ in range(number_of_id):
        print(''.join(random.choices(string.ascii_letters + string.digits, k=number_of_characters)))


user_id_gen_by_user()
# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form


def color_gen():
    return random.randint(0, 255)


def rgb_color_gen():
    return f'rgb({color_gen()},{color_gen()},{color_gen()})'


print(rgb_color_gen())
# Exercises: Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols,
# 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).


def hexa_color_gen():
    return '#' + ''.join(random.choices(string.digits + 'abcdef', k=6))


def list_of_hexa_colors(num):
    lst = []
    for _ in range(num):
        lst.append(hexa_color_gen())
    return lst


# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.


def list_of_rgb_colors(num):
    lst = []
    for _ in range(num):
        lst.append(rgb_color_gen())
    return lst


# Write a function generate_colors which can generate any number of hexa or rgb colors.
# generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
# generate_colors('hexa', 1) # ['#b334ef']
# generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
# generate_colors('rgb', 1)  # ['rgb(33,79, 176)']


def generate_colors(kind, num):
    return list_of_hexa_colors(num) if kind == 'hexa' else list_of_rgb_colors(num)


print(generate_colors('hexa', 3))  # ['#a3e12f','#03ed55','#eb3d2b']
print(generate_colors('hexa', 1))  # ['#b334ef']
print(generate_colors('rgb', 3))   # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
print(generate_colors('rgb', 1))   # ['rgb(33,79, 176)']

# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter, and it returns a shuffled list


def shuffle_list(lst: list):
    random.shuffle(lst)
    return lst


print(shuffle_list([1, 2, 3, 4, 5, 6, 7]))
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.


def random_seven_numbers():
    list_of_numbers = set()
    while len(list_of_numbers) < 7:
        list_of_numbers.add(random.randint(0, 10))
    return list(list_of_numbers)


print(random_seven_numbers())
