max_calories_value = 0

with open("input_data.txt") as file:
    current_calories_sum = 0

    for line in file:
        line = line.strip()

        if line:
            current_calories_sum += int(line)
        else:
            if current_calories_sum > max_calories_value:
                max_calories_value = current_calories_sum
            current_calories_sum = 0

print(max_calories_value)
