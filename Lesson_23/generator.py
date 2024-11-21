import random
from nltk.corpus import words

word_list = list(set(words.words()))


def random_unique_words(count: int):
    if count > len(word_list):
        raise ValueError(f"Maximum number of unique words is {len(word_list)}")

    unique_words = random.sample(word_list, count)

    for word in unique_words:
        yield word


if __name__ == "__main__":
    word_count = 10_000
    generated_words = list(random_unique_words(word_count))

    print(f"Total unique words in NLTK: {len(word_list)}")
    print(f"Generated words count: {len(generated_words)}")
    print(f"Unique generated words count: {len(set(generated_words))}")
    print("\nGenerated Words:")

    for word in generated_words:
        print(word)
