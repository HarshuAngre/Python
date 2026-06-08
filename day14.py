"""from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def add_two_numbers(x, y):
    return int(x) + int(y)

total = reduce(add_two_numbers, numbers)
print(total)

def change_to_upper(name):
    return name.upper()

upper_case_names = map(change_to_upper, countries)
print(list(upper_case_names))

def is_long_names(Name):
    if len(Name) > 7:
        return True
    else:
        return False

long_names = filter(is_long_names, names)
print(list(long_names))"""


"""def add_ten():
    ten = 10
    def add(num):
        return ten + num
    return add

closure_result = add_ten()
print(closure_result(5))


def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_upper_case = func.upper()
        return make_upper_case
    return wrapper
g = uppercase_decorator(greeting)
print(g())

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_upper = func.upper()
        return make_upper    
    return wrapper
@uppercase_decorator
def greetings():
    return 'welcome to python'

print(greetings())


for country in countries:
    print(country)

for name in names:
    print(name)

for num in numbers:
    print(num)

uppercase = map(lambda country: country.upper(),countries)
print(list(uppercase))

square_nums = map(lambda num: num**2, numbers)
print(list(square_nums))

uppercase_names = map(lambda name: name.upper(),names)
print(list(uppercase_names))


def land_names(country):
    if 'land' in country:
        return True
    return False

lands = filter(land_names, countries)
print(list(lands))


def six(country):
    if len(country) >= 6:
        return True
    return False

sixx = filter(six, countries)
print(list(sixx))


def E_names(country):
    if country[0] == 'E':
        return True
    return False

Ename = filter(E_names,countries)
print(list(Ename))


def square(x):
    return x**2
def is_even(x):
    return x % 2 == 0
def add(x,y):
    return x + y

result = reduce(add,filter(is_even,map(square, numbers)))
print(result)"""