from helpers import stripped_line_iter
from current_day_helpers import get_priority_mapping
from string import ascii_lowercase, ascii_uppercase


def get_sum_of_priorities() -> int:
    priority_mapping = get_priority_mapping()
    lines = stripped_line_iter("input_data.txt")

    sum_of_priorities = 0

    while True:
        try:
            group_duplicate_set = set(ascii_lowercase + ascii_uppercase)

            for _ in range(3):
                line = next(lines)
                items = set(line)
                group_duplicate_set &= set(items)

            group_duplicate = group_duplicate_set.pop()
            group_duplicate_value = priority_mapping[group_duplicate]
            sum_of_priorities += group_duplicate_value

        except StopIteration:
            return sum_of_priorities


print(get_sum_of_priorities())
