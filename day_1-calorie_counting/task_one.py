from helpers import stripped_line_iter


def get_max_calories_value(filename: str) -> int:
    max_calories_value, current_calories_sum = 0, 0
    lines = stripped_line_iter(filename)

    for line in lines:
        if line:
            current_calories_sum += int(line)
        else:
            if current_calories_sum > max_calories_value:
                max_calories_value = current_calories_sum
            current_calories_sum = 0

    return max_calories_value


print(get_max_calories_value("input_data.txt"))
