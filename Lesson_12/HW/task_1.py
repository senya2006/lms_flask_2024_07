def new_format(string):
    return f'{int(string):,}'.replace(',', '.')


# Tests
try:
    assert (new_format("1000000") == "1.000.000")
    assert (new_format("100") == "100")
    assert (new_format("1000") == "1.000")
    assert (new_format("100000") == "100.000")
    assert (new_format("10000") == "10.000")
    assert (new_format("0") == "0")
    print("All tests passed successfully!")
except AssertionError:
    print("One or more tests are not passed :( ")
