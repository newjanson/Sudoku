import random
import string

class SudokuBoard:
    def __init__(self):
        self.filename = self._get_random_filename()
        self.board = [[]]
        self.DIMENSION = 9

        f = open(self.filename, "r")
        # Collect each line and split the values into elements of an array
        self.board = [line.split() for line in f.readlines()]

        # Convert the elements in the board from strings to integers
        for i in range(self.DIMENSION):
            for j in range(self.DIMENSION):
                self.board[i][j] = int(self.board[i][j])

        self.board = self.board[:9]
        f.close()

    def _get_random_filename(self):
        num_code = str(random.randint(1, 16).zfill(2))
        letter_code = random.choice(string.ascii_letters[0:2])
        return "dataset/s" + num_code + letter_code + ".txt

    def check_win_condition(self):
        return all((0 not in row) and (sum(row) == 45) for row in self.board)

    def get_board_copy(self):
        return self.board[:]

    def get_element(self, i, j):
        return self.board[i][j]

    def set_element(self, i, j, elem):
        self.board[i][j] = elem
