from helpers import stripped_line_iter
from current_day_helpers import get_ranges


def count_fully_contained_ranges():
    lines = stripped_line_iter("input_data.txt")
    full_range_counter = 0

    for line in lines:
        range_set_a, range_set_b = get_ranges(line)

        if range_set_a.issubset(range_set_b) or range_set_a.issuperset(range_set_b):
            full_range_counter += 1

    return full_range_counter


print(count_fully_contained_ranges())
