"""
The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
What if the string is empty? Then the result should be empty object literal, {}.
"""


def count(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


# Tests
def run_tests():
    print(count('aba'))  # {'a': 2, 'b': 1}
    print(count(''))  # {}
    print(count('aa'))  # {'a': 2}
    print(count('aabb'))  # {'a': 2, 'b': 2}


if __name__ == "__main__":
    run_tests()
