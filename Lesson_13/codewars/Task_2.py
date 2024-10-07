import string


def is_pangram(s):
    s = s.lower()
    alphabet = set(string.ascii_lowercase)
    letters_in_s = set(s)
    return alphabet.issubset(letters_in_s)


# Tests
def run_tests():
    pangrams = [
        "The quick brown fox jumps over the lazy dog.",
        "Cwm fjord bank glyphs vext quiz",
        "Pack my box with five dozen liquor jugs.",
        "How quickly daft jumping zebras vex.",
        "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"
    ]

    non_pangrams = [
        "This isn't a pangram!",
        "abcdefghijklm opqrstuvwxyz",
        "Aacdefghijklmnopqrstuvwxyz"
    ]

    for pangram in pangrams:
        print(is_pangram(pangram))  # True

    for non_pangram in non_pangrams:
        print(is_pangram(non_pangram))  # False


if __name__ == "__main__":
    run_tests()
