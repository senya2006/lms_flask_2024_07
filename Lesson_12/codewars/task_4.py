"""
Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built
with the sides of given length and false in any other case.
(In this case, all triangles must have surface greater than 0 to be accepted).
"""


def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False

    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


# Example
def run_tests():
    print(is_triangle(1, 2, 2))  # True
    print(is_triangle(4, 2, 3))  # True
    print(is_triangle(2, 2, 2))  # True
    print(is_triangle(1, 2, 3))  # False
    print(is_triangle(-5, 1, 3))  # False
    print(is_triangle(0, 2, 3))  # False
    print(is_triangle(1, 2, 9))  # False


if __name__ == "__main__":
    run_tests()
