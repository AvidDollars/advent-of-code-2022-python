from helpers import stripped_line_iter


def get_final_score() -> int:
    lines = stripped_line_iter("input_data.txt")
    return sum(get_round_score(pair) for pair in lines)


def get_round_score(pair: str) -> int:
    combos = {
        "A X": 3, "A Y": 4, "A Z": 8,
        "B X": 1, "B Y": 5, "B Z": 9,
        "C X": 2, "C Y": 6, "C Z": 7
    }
    return combos[pair]


print(get_final_score())
