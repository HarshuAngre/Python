"""age = input('Enter your age: ')
wait = 18 - int(age)

if age >= '18':
    print('you can drive')
else:
    print('wait for ' + str(wait) + ' years to drive')"""


"""my_age = 20
your_age = int(input('enter your age: '))

if my_age > your_age:
    print('I am ' + str(my_age - your_age) + ' years older than you')
elif my_age < your_age:
    print('you are ' + str(your_age - my_age) + ' years older than me')
else: 
    print('we are the same age')

a = int(input('enter a number(a): '))
b = int(input('enter another number(b): '))

if a > b:
    print(str(a) + ' is greater than ' + str(b))
elif a < b:
    print(str(a) + ' is smaller than ' + str(b))
else: 
    print(str(a) + ' and ' + str(b) + ' are equal')

score = int(input('enter your score: '))

if score >= 90 and score <= 100:
    print('A')
elif score >= 80 and score <= 89:
    print('B')
elif score >= 70 and score <= 79:
    print('C')
elif score >= 60 and  score <=69:
    print('D')
elif score >= 0 and score <+ 59:
    print('F')
else: 
    print('Invalid score')

month = input('enter the month(small letters only): ')

if month == 'september' or month == 'october' or month == 'november':
    print('the season is autumn')
elif month == 'december' or month == 'january' or month == 'february':
    print('the season is winter')
elif month == 'march' or month == 'april' or month == 'may':
    print('the season is spring')
elif month == 'june' or month == 'july' or month == 'august':
    print('the season is summer')
else:
    print('Invalid month')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('enter a fruit: ')
if fruit in fruits:
    print('fruit found in the list')
else: 
    fruits.append(fruit)
    print('fruit added to the list')
print(fruits)


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }"""

"""if 'skills' in person:
    print('skills found in the person')
    print(person['skills'])
    print(person['skills'][len(person['skills']) // 2])

if 'skills' in person:
    if 'Python' in person['skills']:
        print('Python is one of the skills')
    else:
        print('Python is not one of the skills')


if 'skills' in person:
    if 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('He is a front end developer')
    elif 'Node' in person['skills'] and 'MongoDB' in person['skills'] and 'Python' in person['skills']:
        print('He is a backend developer')
    elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a fullstack developer')
    else:
        print('unknown title')


if person['is_married'] and person['country'] == 'Finland':
    print(person['first_name'] +' ' + person['last_name'] + ' lives in ' + person['country'] + '. He is married')"""
