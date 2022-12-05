from helpers import line_iter
from current_day_helpers import create_supplies_list, create_list_of_stacks
from collections import deque


class Supplies:
    def __init__(self, filename):
        self._lines_iter = line_iter(filename)
        supplies_list = create_supplies_list(self._lines_iter)
        self.list_of_stacks = create_list_of_stacks(supplies_list)

    def get_top_of_stacks(self):
        return "".join(stack[0] for stack in self.list_of_stacks)

    def execute_instructions(self, day=None):
        for instruction in self._lines_iter:
            taken = deque()

            if instruction.strip():
                count, from_, to = instruction.split(" ")[1::2]
                count, from_, to = int(count), int(from_) - 1, int(to) - 1

                for _ in range(count):
                    item = self.list_of_stacks[from_].popleft()
                    taken.append(item)

                if day == "two":
                    taken.reverse()

                self.list_of_stacks[to].extendleft(taken)


supplies = Supplies("input_data.txt")
supplies.execute_instructions()
print(supplies.get_top_of_stacks())

supplies = Supplies("input_data.txt")
supplies.execute_instructions(day="two")
print(supplies.get_top_of_stacks())
