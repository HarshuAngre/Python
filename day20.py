"""import webbrowser

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

for url in url_lists:
    webbrowser.open_new_tab(url)"""

"""import requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

response = requests.get(url)

print(response)
print(response.status_code)
print(response.headers)
print(response.text)

import requests
from collections import Counter
import re

url = "https://www.gutenberg.org/files/1112/1112.txt"

response = requests.get(url)
text = response.text

# Convert to lowercase and keep only words
words = re.findall(r'\b[a-z]+\b', text.lower())

# Count frequencies
word_count = Counter(words)

# Top 10 words
print(word_count.most_common(10))"""