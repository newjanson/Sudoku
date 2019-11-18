from sudokuBoard import load_puzzle
import os

def test_load_puzzle():
    f = open("fake_puzzle.txt", "w+")
    for i in range(9):
        for j in range(9):
            f.write("0 ")
        f.write("\n")
    f.close()
    assert (len(load_puzzle("fake_puzzle.txt"))==8)
    os.remove("fake_puzzle.txt")

