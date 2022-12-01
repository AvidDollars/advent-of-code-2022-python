import heapq

calories_heap = []

with open("input_data.txt") as file:
    current_calories_sum = 0

    for line in file:
        line = line.strip()

        if line:
            current_calories_sum += int(line)
        else:
            heapq.heappush(calories_heap, current_calories_sum)
            current_calories_sum = 0

print(sum(heapq.nlargest(3, calories_heap)))