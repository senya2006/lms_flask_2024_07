"""
16  -->  1 + 6 = 7
942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""


def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n


# Examples
def run_tests():
    print(digital_root(16))  # 7
    print(digital_root(942))  # 6
    print(digital_root(132189))  # 6
    print(digital_root(493193))  # 2


if __name__ == "__main__":
    run_tests()
