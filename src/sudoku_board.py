import random
import string
import copy

class SudokuBoard:
    def __init__(self):

        self.filename = self._get_random_filename()
        self.board = [[]]
        self.original_board = []
        self.DIMENSION = 9

        f = open(self.filename, "r")

        # Collect each line and split the values into elements of an array
        self.board = [line.split() for line in f.readlines()]

        # Convert the elements in the board from strings to integers
        for i in range(self.DIMENSION):
            for j in range(self.DIMENSION):
                self.board[i][j] = int(self.board[i][j])

        self.board = self.board[:9]

        # Make a copy of the board to keep track of the original board
        self.original_board = copy.deepcopy(self.board)

        f.close()

    def _get_random_filename(self):
        num_code = str(random.randint(1, 15)).zfill(2)
        letter_code = random.choice(string.ascii_letters[0:2])
        return "dataset/s" + num_code + letter_code + ".txt"

    def check_win_condition(self):
        return all((0 not in row) and (sum(row) == 45) for row in self.board)

    def get_element(self, i, j):
        return (self.board[i][j], self.original_board[i][j] != 0)

    def set_element(self, i, j, elem):

        if (self.original_board[i][j] == 0 or elem == 0):
            self.board[i][j] = elem
