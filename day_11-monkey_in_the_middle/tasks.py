from collections import deque
from helpers import stripped_line_iter
import re
from dataclasses import dataclass
from typing import Callable, ClassVar
import operator
from functools import reduce


@dataclass
class Monkey:
    divisibility_product: ClassVar[int]
    task: ClassVar[str]

    items: deque
    operation: Callable
    divisibility_rules: dict
    inspection_counter: int = 0

    def inspect_items(self) -> list:
        output = []

        while self.items:
            item = self.items.popleft()
            item %= self.divisibility_product
            item = self.operation(item) // 3 \
                if self.task == "one" \
                else self.operation(item)

            div_num = self.divisibility_rules["divisible_by"]

            monkey_id = self.divisibility_rules[True] \
                if item % div_num == 0 \
                else self.divisibility_rules[False]

            output.append((monkey_id, item))
            self.inspection_counter += 1

        return output

    def get_new_item(self, item: int) -> None:
        self.items.append(item)


def create_list_of_monkeys() -> list[Monkey]:
    lines = stripped_line_iter("input_data.txt")
    get_number = lambda input_: int(re.search("\d+", input_).group(0))
    monkeys = []

    while True:
        try:
            next(lines)
            items = deque([int(item) for item in re.findall("\d+", next(lines))])

            operation = next(lines).split("new = ")[1]
            operation = eval(f"lambda old: {operation}")

            divisibility_rules = {
                "divisible_by": get_number(next(lines)),
                True: get_number(next(lines)),
                False: get_number(next(lines))
            }

            monkeys.append(Monkey(items, operation, divisibility_rules))
            next(lines)

        except StopIteration:
            return monkeys


def divisibility_product(monkeys: list[Monkey]) -> int:
    all_divisibility_rules = [monkey.divisibility_rules["divisible_by"] for monkey in monkeys]
    return reduce(operator.mul, all_divisibility_rules)


def monkey_business(task: str) -> int:
    monkeys = create_list_of_monkeys()
    Monkey.divisibility_product = divisibility_product(monkeys)
    Monkey.task = task if task == "one" else "two"

    iterations = 20 if task == "one" else 10_000
    for _ in range(iterations):

        for monkey in monkeys:
            items_output = monkey.inspect_items()

            for monkey_id, item in items_output:
                monkeys[monkey_id].get_new_item(item)

    monkeys.sort(key=lambda monkey: monkey.inspection_counter, reverse=True)
    return monkeys[0].inspection_counter * monkeys[1].inspection_counter


task_one_result = monkey_business(task="one")
print(task_one_result)

task_two_result = monkey_business(task="two")
print(task_two_result)
