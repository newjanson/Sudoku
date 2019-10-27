import random
import numpy as np

DIMENSION = 9

# failed attempt lol
#
# class Cell:
#     def __init__(self):
#         self.value = None
#         self.block_num = None
#
#
#
# board = np.array([[Cell() for i in range(9)] for j in range(9)])
# count = 0
# q = 0
# box_arr = []
# for i in range(0, 9, 3):
#     for j in range(0, 9, 3):
#         box_arr.append(board[i:i + 3, j:j + 3].flatten())
#         for elem in board[i:i + 3, j:j + 3].flatten():
#             elem.block_num = count
#         count += 1
#
# #possible values in a sudoku board
# possible_values = np.arange(1, DIMENSION + 1)
#
#
#
# i = 0
# j = 0
# # while i < len(board):
# #     while j < len(board):
# #         print("here")
# #         random_number_works = False
# #         possible_values = np.arange(1, DIMENSION + 1).tolist()
# #         random.shuffle(possible_values)
# #         print(possible_values)
# #         while random_number_works == False:
# #             rand_num = possible_values.pop()
# #             if (rand_num in board[i]) or (rand_num in [board[k][j] for k in range(0, len(board))]) or (rand_num in box_arr[board[i][j].block_num]):
# #                 pass
# #             else:
# #                 print(rand_num)
# #                 random_number_works = True
# #                 board[i][j].value = rand_num
# #         j += 1
# #     i += 1
#
#
# x = np.array([elem.value for sublist in board for elem in sublist])
#
#
# print(x)


f = open("s01a.txt", "r")
lines = [line.split() for line in f.readlines()]
lines = [list(map(int,i)) for i in lines]
lines.pop()
f.close()

def check_win_condition(board):
    return not any(0 in row for row in board)
