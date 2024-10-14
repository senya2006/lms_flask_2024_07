import unittest


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')
        if n < len(self.cache):
            return self.cache[n]
        else:
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)
        return self.cache[n]


def formatted_name(first_name, last_name, middle_name=''):
    if len(middle_name) > 0:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


# Tests
class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_fibonacci_first_elements(self):
        self.assertEqual(self.fibonacci(0), 0)
        self.assertEqual(self.fibonacci(1), 1)

    def test_fibonacci_calculation(self):
        self.assertEqual(self.fibonacci(2), 1)
        self.assertEqual(self.fibonacci(3), 2)
        self.assertEqual(self.fibonacci(4), 3)
        self.assertEqual(self.fibonacci(5), 5)
        self.assertEqual(self.fibonacci(6), 8)

    def test_fibonacci_invalid_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci(-1)
        with self.assertRaises(ValueError):
            self.fibonacci("string")


class TestFormattedName(unittest.TestCase):
    def test_formatted_name_without_middle_name(self):
        result = formatted_name("Taras", "Shevchenko")
        self.assertEqual(result, "Taras Shevchenko")

    def test_formatted_name_with_middle_name(self):
        result = formatted_name("Taras", "Shevchenko", "Grygorovych")
        self.assertEqual(result, "Taras Grygorovych Shevchenko")

    def test_formatted_name_with_lowercase(self):
        result = formatted_name("taras", "shevchenko", "grygorovych")
        self.assertEqual(result, "Taras Grygorovych Shevchenko")


if __name__ == '__main__':
    unittest.main()
