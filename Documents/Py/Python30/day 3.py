"""print(3<2)
print(len('mango') == len('avocado'))

print('True == True: ', True == False)
print('1 is 1: ',1 is 1 )
print('coding' in 'coding for all')
print('B not in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false

age = 20
height = 1.75
complex_number = 1 + 2j

base = float(input('Enter base: '))
height = float(input('Enter height: '))
area_of_Triangle = 0.5 * base * height
print('The area of the triangle is ', area_of_Triangle)

side_a = float(input('Enter side a:'))
side_b = float(input('enter side b: '))
side_c = float(input('enter side c: '))
perimeter_of_traingle = side_a + side_b + side_c
print('The perimeter of the triangle is ', perimeter_of_traingle)


length = int(input('Enter length: '))
breadth = int(input('enter breadth: '))
area = length * breadth
perimeter = 2 * (length + breadth)
print('The area of the rectangle is ', area)
print('The perimeter of the rectangle is ', perimeter)

x1,y1 = 2,2
x2,y2 = 6,10

m = (y2 - y1) / x2- x1
print('The slope of the line is ', m)

euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print('The Euclidean distance is ', euclidean_distance)

word1 = 'python'
word2 = 'dragon'
len_word1 = len(word1)
len_word2 = len(word2)
print('python > dragon:', len_word1 > len_word2)
print('Is "on" in both "python" and "dragon"? ', 'on' in word1 and 'on' in word2)

print('jargon' in 'I hope this course is not full of jargon.')

word = 'python'
length = len(word)
print('The length of the word is ', length)

#covert
length_float = float(length)
print('The length of the word as a float is ', length_float)
length_str = str(length)
print('The length of the word as a string is ', length_str)

num = int(input('Enter a number: '))
if num % 2 == 0:
    print(num, 'is an even number')
else:
    print(num, 'is an odd number')

floor_division = 7 // 3
print('The floor division of 7 by 3 is ', floor_division)

print(floor_division == int(7//3)) 

print(type(10) == type('10')) # False - because the data types are different
print(int(9.8) == 10)


Hours = int(input('Enter Hours worked: '))
Rate = int(input('Enter Rate per hour: '))

Pay = Hours * Rate
print('Your Pay is: ', Pay)"""


Years = int(input('Enter number of years you have lived: '))
Seconds = Years * 365 * 24 * 60 * 60
print('You have lived for ', Seconds, ' seconds.')