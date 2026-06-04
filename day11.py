"""def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(3, 5))

def area_of_circle(r):
    pi = 3.14
    return pi * r * r
print(area_of_circle(4))

def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(add_all_nums(1,2,3,4,5))


def convert_c_to_f(celsius):
    F=(celsius *9/5 + 32)
    return F
print(convert_c_to_f(30))

def check_season(month):
    if month in ['december', 'january', 'february']:
        return 'winter'
    elif month in ['march', 'april', 'may']:
        return 'spring'
    elif month in ['june', 'july', 'august']:
        return 'summer'
    elif month in ['september', 'october', 'november']:
        return 'autumn'
    else:
        return 'invalid month'
print(check_season('march'))


def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return 'undefined'
    else:
        slope = (y2 - y1) / (x2 - x1)
        return slope
print(calculate_slope(1, 2, 3, 4))


def print_list(list):
    for item in list:
        print(item)
print_list([1, 2, 3, 4, 5])


rev_list = [1, 2, 3, 4, 5]
def reverse_list(rev_list):
    return rev_list[::-1]
print(reverse_list(rev_list))


def capitalize_list(list):
    capitalized_list = []
    for item in list:
        capitalized_list.append(item.capitalize())
    return capitalized_list
print(capitalize_list(['hello', 'world', 'python']))

item_list = ['mango', 'orange', 'banana']
def add_item(item_list, item):
    item_list.append(item)
    return item_list
print(add_item(item_list, 'grape'))

item_list = ['mango', 'orange', 'banana']
def remove_item(item_list, item):
    if item in item_list:
        item_list.remove(item)
    return item_list
print(remove_item(item_list, 'orange'))

def sum_of_numbers(num):
    total=0
    for i in range(num+1):
        total += i
    return total
print(sum_of_numbers(5))


def sum_of_evens(num):
    total = 0
    for i in range(num+1):
        if i % 2 == 0:
            total += i
    return total
print(sum_of_evens(10))

def evens_and_odds(num):
    odds = 0
    evens = 0
    for i in range(num+1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f'The number of odds are {odds}. The number of evens are {evens}.'
print(evens_and_odds(100))

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(5))

def is_empty(value):
    if value:
        return False
    else:
        return True
print(is_empty('2'))
""" 
from unicodedata import name


list = [1, 2, 3, 4, 5, 6]
"""
def mean(list):
    total = sum(list)
    count = len(list)
    return total/count
print(mean(list))

def median(list):
    list.sort()
    n = len(list)
    if n % 2 == 0:
        median =(list[n//2 - 1] + list[n//2]) / 2
    else:     
        median = list[n//2]
    return median
print(median(list))


def mode(list):
    frequency ={}
    for item in list:
        if item in frequency:
            frequency[item] =+ 1
        else:       
            frequency[item] = 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    return modes
print(mode(list))

def greet(name =  'guest'):
    return f'Hello, {name}!'
print(greet())


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(7))

list= [1, 2, 3, 4, 5, 6]
def is_unique(list):
    return len(list) == len(set(list))
print(is_unique(list))"""