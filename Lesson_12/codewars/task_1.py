"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers
in the form of a phone number.
Example: create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
"""


def create_phone_number(numbers):
    numbers_str = ''.join(map(str, numbers))
    return f"({numbers_str[:3]}) {numbers_str[3:6]}-{numbers_str[6:]}"


# Examples
def run_tests():
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # (123) 456-7890
    print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))  # (111) 111-1111
    print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))  # (023) 056-0890
    print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # (000) 000-0000


if __name__ == "__main__":
    run_tests()
