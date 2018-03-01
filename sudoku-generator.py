"""

"""

# use __future__ to provide compatibility with python 3
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math


def creatematrix(w, h, initialval):
    matrix = [[initialval for x in range(w)] for y in range(h)]
    return matrix


def printmatrix(matrix):
    for row in matrix:
        print(row)


def printmatrixhex(matrix):
    """
    Prints a 16 x 16 sudoku matrix with grid lines
    """
    lookup = ["0", "1", "2", "3", "4", "5", "6",
              "7", "8", "9", "a", "b", "c", "d", "e", "f", "-"]
    output = ""
    row_num = 0
    output += "-" * 61 + "\n"
    for row in matrix:
        output += "|  "
        col_num = 0
        for value in row:
            output += lookup[value] + "  "
            if col_num % 4 == 3:
                output += "|  "
            col_num += 1
        output += "\n"
        if (row_num % 4 == 3):
            output += "-" * 61 + "\n"
        row_num += 1
    print(output)


def checkrows(matrix, size):
    """
    Checks if each row contains each value only once
    """
    row_num = 0
    for row in matrix:
        numbercontained = [False for x in range(size)]
        for value in row:
            # if placeholder, ignore it
            if value in range(size):
                if numbercontained[value]:
                    print(
                        "Number {0} occurs more than once in row {1}!".format(value, row_num))
                    return False
                else:
                    numbercontained[value] = True
        row_num += 1
    print("rows are fine")
    return True


def checkcols(matrix, size):
    """
    Checks if each column contains each value only once
    """
    for col_num in range(size):
        numbercontained = [False for x in range(size)]
        for row_num in range(size):
            value = matrix[row_num][col_num]
            # if placeholder, ignore it
            if value in range(size):
                if numbercontained[value]:
                    print(
                        "Number {0} occurs more than once in col {1}!".format(value, col_num))
                    return False
                else:
                    numbercontained[value] = True
    print("cols are fine")
    return True


def checkblocks(matrix, size):
    """
    Checks if each block contains each value only once
    """
    blocksize = math.sqrt(size)
    print(blocksize)
    for block_num in range(size):
        numbercontained = [False for x in range(size)]
        for value_num in range(size):
            row_num =
            value = matrix[row_num % blocksize][val % blocksize]
            # if placeholder, ignore it
            if value in range(size):
                if numbercontained[value]:
                    print(
                        "Number {0} occurs more than once in block {1}!".format(value, block_num))
                    return False
                else:
                    numbercontained[value] = True
    print("blocks are fine")
    return True


def main():
    matrix = creatematrix(16, 16, 16)
    printmatrixhex(matrix)
    checkrows(matrix, 16)
    checkcols(matrix, 16)


if __name__ == "__main__":
    main()
