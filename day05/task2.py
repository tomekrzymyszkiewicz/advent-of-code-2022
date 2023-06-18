import re


def load_crates(lines: list[str]) -> list[list[str]]:
    crates_horizontally = [
        [char for i, char in enumerate(line[1:-1]) if i % 4 == 0] for line in lines
    ]
    number_of_crates = len(crates_horizontally[0])
    crates_lists = [[] for _ in range(number_of_crates)]
    for row in reversed(crates_horizontally):
        for i, char in enumerate(row):
            if char != " ":
                crates_lists[i].append(char)
    return crates_lists


def load_moves(lines: list[str]) -> list[list[int]]:
    moves_list = [list(map(int, re.findall(r"\d+", line))) for line in lines]
    return moves_list


def make_moves(crates: list[list[str]], moves: list[list[int]]) -> list[list[str]]:
    for move in moves:
        crates[move[2] - 1].extend(crates[move[1] - 1][-move[0] :])
        crates[move[1] - 1] = crates[move[1] - 1][: -move[0]]
    return crates


with open("input.txt") as f:
    lines = f.read().splitlines()
crates = load_crates(lines[: lines.index("") - 1])
moves = load_moves(lines[lines.index("") + 1 :])
print("".join(crate[-1] for crate in make_moves(crates, moves)))
