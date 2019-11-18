from typing import List

DIMENSION = 9

def load_puzzle(filename: str) -> List[int]:
    f = open(filename, "r")
    lines = [line.split() for line in f.readlines()]
    lines = [list(map(int,i)) for i in lines]
    lines.pop()
    f.close()
    return lines

def check_win_condition(board):
    return not any(0 in row for row in board)
