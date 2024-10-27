# import nltk

# Loading the word list
# nltk.download('words')

import random
from nltk.corpus import words

# Download a big list of words
word_list = words.words()


def random_unique_words(count: int):
    if count > 10_000:
        raise ValueError("Maximum number of words — 10_000")

    unique_words = random.sample(word_list, count)

    for word in unique_words:
        yield word


# Example
word_count = 10_000
for word in random_unique_words(word_count):
    print(word)
