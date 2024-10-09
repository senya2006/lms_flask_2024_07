def max_water_depth(heights):
    if not heights:
        return 0

    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n

    # Filling the array left_max
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    # Filling the array right_max
    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    # Calculating the depth of the deepest depression
    max_depth = 0
    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        depth = water_level - heights[i]
        max_depth = max(max_depth, depth)

    return max_depth


# Tests
def run_tests():
    print(max_water_depth([1, 2, 1, 2, 1]))  # 1
    print(max_water_depth([3, 0, 2, 0, 4]))  # 4
    print(max_water_depth([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 2
    print(max_water_depth([5, 4, 3, 2, 1, 2, 3, 4, 5]))  # 4
    print(max_water_depth([4, 1, 1, 0, 2, 3]))  # 3
    print(max_water_depth([2, 0, 2]))  # 2
    print(max_water_depth([5]))  # (only one peak)
    print(max_water_depth([]))  # 0 (empty array)


if __name__ == "__main__":
    run_tests()
