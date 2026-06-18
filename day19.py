"""import json

def most_spoken_language(filename, n):
    with open(filename, 'r', encoding = 'utf-8') as file:
        countries = json.load(file)

        language_count = {}

        for country in countries:
            for language in country['languages']:
                language_count[language] = language_count.get(language, 0) + 1


        sorted_language = sorted(
            language_count.items(),
            key = lambda item: item[1],
            reverse=True
        )

        return[(count,language) for language, count in sorted_language[:n]]

print(most_spoken_language(
    'C:/Users/HarshuAngre/Downloads/countries_data.json', 3
))"""


"""import json

def most_populated_countries(filename,n):
    with open(filename,'r',encoding='utf-8') as file:
        countries = json.load(file)

    sorted_countries = sorted(
        countries,
        key = lambda country: country['population'],
        reverse = Truext
    )

    result = []

    for country in sorted_countries[:n]:
        result.append({
            'country': country['name'],
            'population': country['population']
        })
    return result

print(most_populated_countries(
    'C:/Users/HarshuAngre/Downloads/countries_data.json', 3
))


import re

with open('C:/Users/HarshuAngre/Downloads/email_exchanges_big.txt','r', encoding = 'utf-8') as file:
    text = file.read()

    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+',text)

print(emails)
print('total emails:',len(emails))

'C:/Users/HarshuAngre/Downloads/obama_speech.t'"""


"""import re


def most_frequent_words(filename,n):
    with open(filename,'r',encoding = 'utf-8') as file:
        text = file.read().lower()

    words = re.findall(r'\b[a-z]+\b',text)

    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word,0) + 1
    
    sorted_words = sorted(
        word_count.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_words[:n]

print(most_frequent_words(
    'C:/Users/HarshuAngre/Downloads/obama_speech.txt', 3
))"""
