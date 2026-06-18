import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]','', text)
    return text

def remove_support_words(text, stop_word):
    words = text.split()
    return[word for word in words if word not in stop_words]

def check_text_similarity(text1,text2,stop_words):
    text1 = clean_text(text1)
    text2 = clean_text(text2)

    words1 = set(remove_support_words(text1,stop_words))
    words2 =set(remove_support_words(text2,stop_words))

    common_words = words1.intersection(words2)
    total_words = words1.union(words2)

    similarity = len(common_words) / len(total_words) *100

    return similarity

with open(
    'C:/Users/HarshuAngre/Downloads/stop_words.py',
    'r',
    encoding='utf-8'
    ) as file:
        stop_words = file.read().split(',')

with open(
    'C:/Users/HarshuAngre/Downloads/michelle_obama_speech.txt',
    'r',
    encoding='utf-8'
) as file: 
        michelle = file.read()

with open(
    'C:/Users/HarshuAngre/Downloads/melina_trump_speech.txt',
    'r',
    encoding='utf-8'
) as file:
      melina = file.read()


similarity = check_text_similarity(
      michelle,
      melina,
      stop_words
)

print(f"similarity: {similarity:.2f}%")
