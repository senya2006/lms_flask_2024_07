def sum_of_intervals(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort by the beginning of the interval
    total_sum = 0
    current_start, current_end = intervals[0]  # Let's take the first interval

    for start, end in intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)  # Update the end if it overlaps
        else:
            total_sum += current_end - current_start
            current_start, current_end = start, end

    total_sum += current_end - current_start
    return total_sum


# Tests
if __name__ == "__main__":
    print(sum_of_intervals([(1, 5)]))  # 4
    print(sum_of_intervals([(1, 5), (6, 10)]))  # 8
    print(sum_of_intervals([(1, 5), (1, 5)]))  # 4
    print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))  # 7
    print(sum_of_intervals([(1, 2), (6, 10), (11, 15)]))  # 9
    print(sum_of_intervals([(0, 20), (-100000000, 10), (30, 40)]))  # 100000030
