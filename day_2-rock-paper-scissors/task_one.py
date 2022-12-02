from helpers import stripped_line_iter


def get_final_score() -> int:
    lines = stripped_line_iter("input_data.txt")
    return sum(get_round_score(pair) for pair in lines)


def get_round_score(pair: str) -> int:
    combos = {
        "A X": 4, "A Y": 8, "A Z": 3,
        "B X": 1, "B Y": 5, "B Z": 9,
        "C X": 7, "C Y": 2, "C Z": 6
    }
    return combos[pair]


print(get_final_score())
