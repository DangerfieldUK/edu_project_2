import requests
from collections import Counter
import string
import re

data = requests.get('https://baconipsum.com/api/?type=all-meat').json()
text = " ".join(data).lower()
text = re.sub("[^\w-]", " ", text)

matches = re.findall(r'[a-zA-Z]+[-]?[a-zA-Z]*', text)

commonwords = Counter(matches).most_common(5)

print('\nThe most common words are:')
for word, count in commonwords:
   print(f'{word} : {count}')