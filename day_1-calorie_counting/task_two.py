import heapq

from helpers import stripped_line_iter


def get_sum_for_nlargest_calories(filename: str, n_largest: int) -> int:
    calories_heap = []
    current_calories_sum = 0

    lines = stripped_line_iter(filename)

    for line in lines:
        if line:
            current_calories_sum += int(line)
        else:
            heapq.heappush(calories_heap, current_calories_sum)
            current_calories_sum = 0

    return sum(heapq.nlargest(n_largest, calories_heap))


print(get_sum_for_nlargest_calories("input_data.txt", n_largest=3))
