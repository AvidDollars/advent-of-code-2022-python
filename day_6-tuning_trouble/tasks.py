from current_day_helpers import n_chars_iter_enumerated


def detect_marker(part=None):
    n_chars = 14 if part == "two" else 4
    packets = n_chars_iter_enumerated("input_data.txt", n_chars=n_chars)

    for packet in packets:
        unique_chars = {char for idx, char in packet}

        if len(unique_chars) == n_chars:
            last_index = packet[-1][0]
            return last_index


print(detect_marker(part="one"))
print(detect_marker(part="two"))
