"""numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero = [i for i in numbers if i <= 0]

print(negative_zero)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattend_lst = [number for row in list_of_lists for number in row]
print(flattend_lst)

result = [(n, n**0, n**1, n**2, n**3, n**4, n**5) for n in range(11)]


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

result = [
    {'country': country.upper(), 'city': city.upper()}
    for [(country, city)] in countries]

print(result)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

result = [first +' ' + last for [(first, last)] in names]
print(result)

slope = lambda x1,y1,x2,y2 : (y2-y1) / (x2-x1)

print(slope(2,3,10,8))"""