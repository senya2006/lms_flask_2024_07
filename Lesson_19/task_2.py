"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    words = text.split()
    result = [
        word[1:] + word[0] + "ay" if word.isalpha() else word
        for word in words
    ]
    return ' '.join(result)


# Tests
def run_tests():
    print(pig_it('Pig latin is cool'))  # "igPay atinlay siay oolcay"
    print(pig_it('Hello world !'))  # "elloHay orldway !"
    print(pig_it('This is my string'))  # "hisTay siay ymay tringsay"
    print(pig_it('Testing, punctuation!'))  # "estingTay, unctuationpay!"


if __name__ == "__main__":
    run_tests()
