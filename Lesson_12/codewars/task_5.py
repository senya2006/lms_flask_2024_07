"""
Your goal in this kata is to implement a difference function, which subtracts one list from another
and returns the result.
It should remove all values from list a which are present in list b keeping their order.
array_diff([1,2],[1]) == [2]
"""


def array_diff(a, b):
    return [item for item in a if item not in b]


def run_tests():
    print(array_diff([1, 2], [1]))  # [2]
    print(array_diff([1, 2, 2], [1]))  # [2, 2]
    print(array_diff([1, 2, 2], [2]))  # [1]
    print(array_diff([1, 2, 2], []))  # [1, 2, 2]
    print(array_diff([], [1, 2]))  # []
    print(array_diff([1, 2, 3], [1, 2]))  # [3]


if __name__ == "__main__":
    run_tests()
