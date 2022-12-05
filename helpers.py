def stripped_line_iter(filename):
    with open(filename) as file:
        for line in file:
            yield line.strip()


def line_iter(filename):
    with open(filename) as file:
        for line in file:
            yield line.strip("\n")
