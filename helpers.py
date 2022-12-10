def stripped_line_iter(filename):
    with open(filename) as file:
        for line in file:
            yield line.strip()


def line_iter(filename):
    with open(filename) as file:
        for line in file:
            yield line.strip("\n")


def try_parse_number(input_):
    try:
        parsed_number = int(input_)
    except ValueError:
        return False, None
    else:
        return True, parsed_number
