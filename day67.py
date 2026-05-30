"""brothers = ('harshu', 'pratik', 'sourav', 'tanish')
sisters = ('sneha', 'priya', 'surbhi', 'tanya')
siblings = brothers + sisters
print(siblings)
print(len(siblings))
family_members = siblings + ('mummy', 'papa')
print(family_members)
family = family_members[8:10] 
print(family)
others = family_members[:8]
print(others)

fruits = ['apple', 'banana', 'cherry', 'mango', 'melon']
vegetables = ['carrot', 'broccoli', 'spinach', 'cabbage', 'cauliflower']
animals = ['chicken', 'goat', 'sheeps', 'rabbit', 'duck']
food_stuff_tp = fruits + vegetables + animals

food_stuff_lt = list(food_stuff_tp)

print(food_stuff_lt[int(len(food_stuff_lt)/2)])
print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])

del food_stuff_lt

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)


#DAY 7

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]"""

"""print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['linkedin', 'netflix', 'uber'])
it_companies.remove('IBM') #raises error if element not found
it_companies.discard('oracl') #does not raise error if element not found

A.union(B)
print(A.intersection(B))
print(A.issubset(B))

B.union(A)

C = A.symmetric_difference(B)
print(C)

del A,B

age_set = set(age)
print(age_set)

print(len(age_set))
print(len(age))

bigger = len(age) > len(age_set)
print(bigger)

str1 = 'I am a teacher and I love to inspire and teach people'
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

str1_set = set(str1.split())
print(str1_set)
print(len(str1_set))"""