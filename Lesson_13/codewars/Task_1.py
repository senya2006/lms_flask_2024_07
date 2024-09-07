"""
For example, take 153 (3 digits), which is narcissistic:
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1652 (4 digits), which isn't:
    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
"""


def narcissistic(value):
    digits = [int(digit) for digit in str(value)]
    num_digits = len(digits)
    narcissistic_sum = sum([digit ** num_digits for digit in digits])
    return narcissistic_sum == value


# Tests
def run_tests():
    print(narcissistic(7))  # True
    print(narcissistic(371))  # True
    print(narcissistic(122))  # False
    print(narcissistic(4887))  # False


if __name__ == "__main__":
    run_tests()
