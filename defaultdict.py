
from collections import defaultdict

def count_words(text):
    count = defaultdict(int)
    for word in text.split():
        count[word] += 1
    return count




