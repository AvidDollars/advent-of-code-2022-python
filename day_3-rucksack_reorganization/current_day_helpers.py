def get_priority_mapping() -> dict:
    lowercase_start, uppercase_start = ord("a"), ord("A")

    lowercase_mapping = {
        chr(num): num - lowercase_start + 1
        for num in range(lowercase_start, lowercase_start + 26)
    }

    uppercase_mapping = {
        chr(num): num - uppercase_start + 1 + 26
        for num in range(uppercase_start, uppercase_start + 26)
    }

    lowercase_mapping.update(uppercase_mapping)
    return lowercase_mapping


def get_duplicate_value(input_) -> str:
    middle = int(len(input_) / 2)
    compartment_a, compartment_b = input_[:middle], input_[middle:]
    duplicate_set = set(compartment_a) & set(compartment_b)
    duplicate = duplicate_set.pop()
    return duplicate
