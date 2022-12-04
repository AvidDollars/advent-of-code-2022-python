def create_range_from_str(range_str: str) -> range:
    start, stop = range_str.split("-")
    start, stop = int(start), int(stop) + 1
    return range(start, stop)


def get_ranges(ranges_str: str) -> tuple[set, set]:
    range_a, range_b = ranges_str.split(",")

    return (
        set(create_range_from_str(range_a)),
        set(create_range_from_str(range_b))
    )