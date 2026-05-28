"""print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # """

"""word1 = 'thirty'
word2 = 'days'
word3 = 'of'
word4 = 'python'
sentence = word1 + ' ' + word2 + ' ' + word3 + ' ' + word4
print(sentence) # thirty days of python"""


word1 = 'Coding'
word2 = 'for' 
word3 = 'all'
company = word1 + ' ' + word2 + ' ' + word3  
"""print(company) # Coding for all
print(len(company))
print(company.upper())
print(company.lower())

print(company.capitalize()) # Coding for all
print(company.title()) # Coding For All
print(company.swapcase()) # cODING FOR ALL

print(company[0:6]) # Coding
print(company.find('Coding')) # 0

print(company.replace('Coding', 'Python')) # Python for all
print(company.replace('Coding', 'Python').replace('all', 'everyone')) # Python for everyone

print(company.split()) # ['Coding', 'for', 'all']
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(', '))

CFA = company
print(CFA) # C
PFA = company.replace('Coding', 'Python')
print(PFA) # Python for all

print(company.index('C')) # 0  
print(company.index('f')) # 7
print('Coding for all people'.rindex('l')) 

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.rindex('because'))

print(sentence[31:54]) # because because because

sub_str = 'Coding'
print(company.startswith(sub_str)) # True
print(company.endswith('coding')) # False

spaces = '   Coding for all      '
print(spaces.strip()) # 'Coding for all'
print(spaces.lstrip()) # 'Coding for all      '


challenge = 'thirtydaysofpython'
print(challenge.isidentifier())
challenge2 = '30DaysOfPython'
print(challenge2.isidentifier())

list = ['django', 'flask', 'python', 'java', 'c++']
print(' # '.join(list)) # django # flask # python # java # c++

print('I am enjoying this challenge.\nI just wonder what is next.')

print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
print('the area of circle with radius {} is {}'.format(radius,area)) # the area of circle with radius 10 is 314.0"""


a= 8
b= 6
c= a + b
print('{} + {} = {}'.format(a,b,c))
print('{} - {} = {}'.format(a,b,c))
print('{} * {} = {}'.format(a,b,c))
print('{} / {} = {}'.format(a,b,c))
print('{} % {} = {}'.format(a,b,c))
print('{} // {} = {}'.format(a,b,c))
print('{} ** {} = {}'.format(a,b,c))
