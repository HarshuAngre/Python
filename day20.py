import re

"""with open(
    'C:/Users/HarshuAngre/Downloads/romeo_and_juliet.txt',
    'r',
    encoding = 'utf-8'
) as file:
    text = file.read().lower()


words = re.findall(r'\b[a-z]+\b',text)

word_count = {}

for word in words:
    word_count[word] = word_count.get(word,0) + 1


sorted_words = sorted(
    word_count.items(),
    key= lambda item:item[1],
    reverse= True
)

print(sorted_words[:10])"""

import csv

count = 0

with open(
    'C:/Users/HarshuAngre/Downloads/hacker_news.csv',
    'r',
    encoding='utf-8'
) as file:
    reader = csv.reader(file)

    for row in reader:
        row_text = ''.join(row)
        if 'python' in row_text.lower():
            count += 1

print(count)