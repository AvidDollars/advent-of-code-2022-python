from collections import deque
from helpers import try_parse_number


def parse_floor(floor):
    parsed = []
    floor_iter = iter(floor)

    while True:
        try:
            for item in range(4):
                next(floor_iter)

                if item := next(floor_iter):
                    parsed.append(item)
                else:
                    parsed.append(" ")

                next(floor_iter), next(floor_iter)
        except StopIteration:
            return parsed


def create_supplies_list(lines_iter):
    supplies_stack_list = []

    for line in lines_iter:
        parsed_floor = parse_floor(line)

        last_value = parsed_floor[-1]
        was_parsed, column_count = try_parse_number(last_value)

        if was_parsed:  # line with numbers was encountered
            break

        supplies_stack_list.append(parsed_floor)

    for floor in supplies_stack_list:
        remaining = column_count - len(floor)
        for _ in range(remaining):
            floor.append(" ")

    return supplies_stack_list


def create_list_of_stacks(supplies_list):
    column_count = len(supplies_list[0])
    list_of_stacks = [deque() for _ in range(column_count)]

    for row_idx, row in enumerate(supplies_list):
        for col_idx, element in enumerate(row):
            if element.strip():
                list_of_stacks[col_idx].append(element)

    return list_of_stacks
