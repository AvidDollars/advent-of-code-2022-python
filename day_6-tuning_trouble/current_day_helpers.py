from collections import deque


def n_chars_iter_enumerated(filename: str, n_chars: int) -> list[str]:
    with open(filename) as file:

        try:
            line = next(file)
            line_iter = iter(line)

            current_four = deque(
                [
                    (index, next(line_iter))
                    for index, _
                    in enumerate(range(n_chars), 1)
                ]
            )

            yield current_four  # 1st iteration

            while True:
                old_index, _ = current_four.popleft()
                current_four.append((old_index + n_chars, next(line_iter)))

                yield current_four  # 2nd to last iteration

        except StopIteration:
            return current_four
