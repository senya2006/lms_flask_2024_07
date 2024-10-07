"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
Note: If the number is a multiple of both 3 and 5, only count it once.
"""


def solution(number):
    if number < 0:
        return 0
    multiples = [i for i in range(number) if i % 3 == 0 or i % 5 == 0]
    return sum(multiples)


# Tests
def run_tests():
    print(solution(4))  # 3
    print(solution(6))  # 8
    print(solution(16))  # 60
    print(solution(3))  # 0
    print(solution(5))  # 3
    print(solution(15))  # 45
    print(solution(0))  # 0
    print(solution(-1))  # 0
    print(solution(10))  # 23
    print(solution(20))  # 78
    print(solution(200))  # 9168


if __name__ == "__main__":
    run_tests()
