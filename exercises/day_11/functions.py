"""Day 11: 30 Days of python programming"""


# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.


def add_two_numbers(a, b):
    """ Returns the sum of two numbers"""
    return a + b


print(add_two_numbers(1, 2))


def area_of_circle(r):
    """
    Area of a circle is calculated as follows: area = π x r x r. 
    Write a function that calculates area_of_circle.
    """
    return 3.14 * r * r


print(area_of_circle(3))


def add_all_nums(*nums):
    """
    Write a function called add_all_nums which takes arbitrary number of arguments,
    and sums all the arguments.
    Check if all the list items are number types. If not do give a reasonable feedback.
    """
    suma = 0
    for num in nums:
        if isinstance(num, int):
            suma += num
        else:
            print(num, 'is not a number')
    print('The sum is', suma)


add_all_nums(1, 2, 3, 'a')


def convert_celsius_to_fahrenheit(c):
    """
    Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
    Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
    """
    return ((c * 9.0) / 5) + 32


print(convert_celsius_to_fahrenheit(20))


def check_season(month):
    """
    Write a function called check-season,
    it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
    """
    if month in range(1, 3) or month == 12:
        return 'Winter'
    elif month in range(3, 6):
        return 'Spring'
    elif month in range(6, 9):
        return 'Summer'
    elif month in range(9, 12):
        return 'Autumn'
    else:
        return 'Unknown'


print(check_season(1))
print(check_season(3))
print(check_season(6))
print(check_season(9))
print(check_season(12))
print(check_season(13))


def calculate_slope(a, b):
    """
    Write a function called calculate_slope which return the slope of a linear equation
    """
    return (a[0] - b[0]) * (a[1] - b[1]) ** -1


def solve_quadratic_eqn(nepe):
    """
    Quadratic equation is calculated as follows: ax² + bx + c = 0.
    Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
    """
    return nepe


def print_list(lst):
    """
    Declare a function named print_list. 
    It takes a list as a parameter, and it prints out each element of the list.
    """
    for item in lst:
        print(item)


print_list([1, 2, 3])


def reverse_list(lst):
    """
    Declare a function named reverse_list.
    It takes an array as a parameter, and it returns the reverse of the array (use loops).
    print(reverse_list([1, 2, 3, 4, 5]))
    # [5, 4, 3, 2, 1]
    print(reverse_list1(["A", "B", "C"]))
    # ["C", "B", "A"]
    """
    rvs = []
    for i in range(len(lst), 0, -1):
        rvs.append(lst[i])
    return rvs


def capitalize_list_items(lst: list):
    """
    Declare a function named capitalize_list_items.
    It takes a list as a parameter, and it returns a capitalized list of items
    """
    for i, item in enumerate(lst):
        if isinstance(item, str):
            lst[i] = item.capitalize()
    return lst


print(capitalize_list_items(["house", 2]))


def add_item(lst, item):
    """
    Declare a function named add_item.
    It takes a list and an item parameters. It returns a list with the item added at the end.
    food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
    print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
    numbers = [2, 3, 7, 9];
    print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
    """
    if isinstance(lst, list):
        lst.append(item)
    return lst


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))  # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))


def remove_item(lst: list, item):
    """
    Declare a function named remove_item.
    It takes a list and an item parameters. It returns a list with the item removed from it.
    food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
    print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
    numbers = [2, 3, 7, 9];
    print(remove_item(numbers, 3))  # [2, 7, 9]
    """
    lst.remove(item)
    return lst


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))


def sum_of_numbers(num):
    """
    Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.xdfsadddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    print(sum_of_numbers(5))  # 15
    print(sum_all_numbers(10)) # 55
    print(sum_all_numbers(100)) # 5050
    """
    return sum(range(num))


print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))


def sum_of_odds(*nums):
    """
    Declare a function named sum_of_odds.
    It takes a number parameter, and it adds all the odd numbers in that range.
    """
    sum = 0
    for num in nums:
        if num % 2 != 0:
            sum += num
    return sum


def sum_of_even(*nums):
    """
    Declare a function named sum_of_even.
    It takes a number parameter, and it adds all the even numbers in that range.
    """
    sum = 0
    for num in nums:
        if num % 2 == 0:
            sum += num
    return sum


print(sum_of_even(1, 2, 3, 4, 5))
print(sum_of_odds(1, 2, 3, 4, 5))
# Exercises: Level 2


def evens_and_odds(num):
    """
    Declare a function named evens_and_odds.
    It takes a positive integer as parameter, and it counts number of evens and odds in the number.
    # print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
    """
    odds = 0
    evens = 0
    for i in range(num+1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f'The number of odds are {odds}.')
    print(f'The number of evens are {evens}.')


evens_and_odds(100)


def factorial(num):
    """
    Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
    """
    total = 1
    for n in range(1, num+1):
        total *= n
    return total


print(factorial(5))
# Call your function is_empty, it takes a parameter and it checks if it is empty or not


def is_empty(it):
    return True if len(it) == 0 else False


print(is_empty([1, 2, 3]))
print(is_empty([]))
