class CustomMapIterator:
    def __init__(self, data: dict, func1, func2):
        self.data = data
        self.func1 = func1
        self.func2 = func2
        # Convert the dictionary to a list of pairs (key, value)
        self.keys_values = list(data.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.keys_values):
            raise StopIteration
        key, value = self.keys_values[self.index]
        transformed_key = self.func1(key)
        transformed_value = self.func2(value)
        self.index += 1

        return transformed_key, transformed_value


# Example
def uppercase_key(key):
    return key.upper()


def multiply_value(value):
    return value * 2


my_dict = {'a': 1, 'b': 2, 'c': 3}

# Create iterator instance
custom_map = CustomMapIterator(my_dict, uppercase_key, multiply_value)

for key, value in custom_map:
    print(f"Key: {key}, Value: {value}")
