from helpers import stripped_line_iter
from current_day_helpers import get_priority_mapping, get_duplicate_value


def get_sum_of_duplicates() -> int:
    priority_mapping = get_priority_mapping()
    lines = stripped_line_iter("input_data.txt")

    duplicate_sum = 0

    for line in lines:
        duplicate = get_duplicate_value(line)
        value = priority_mapping[duplicate]
        duplicate_sum += value

    return duplicate_sum


print(get_sum_of_duplicates())
