"""
Here's the deal:
It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""


def generate_hashtag(s):
    if not s.strip():
        return False
    hashtag = '#' + ''.join(word.capitalize() for word in s.split())
    if len(hashtag) > 140:
        return False
    if hashtag == '#':
        return False

    return hashtag


# Tests
def run_tests():
    print(generate_hashtag("Hello there thanks for trying my Kata"))
    # #HelloThereThanksForTryingMyKata

    print(generate_hashtag("    Hello     World   "))
    # #HelloWorld

    print(generate_hashtag(""))
    # False

    print(generate_hashtag("a" * 140))
    # False

    print(generate_hashtag("    "))
    # False


if __name__ == "__main__":
    run_tests()
