
class SudokuBoard:
    def __init__(self, filename):
        f = open(filename, "r")
        self.board = [line.split() for line in f.readlines()]
        self.board = [list(map(int, i)) for i in self.board]
        self.board.pop()
        f.close()

    def check_win_condition(board):
        return not any(0 in row for row in board)
