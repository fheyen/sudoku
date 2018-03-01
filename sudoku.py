"""
Sudoku generator
"""

# use __future__ to provide compatibility with python 3
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import math
import random


def creatematrix(w, h, initialval):
    matrix = [[initialval for x in range(w)] for y in range(h)]
    return matrix


def createemptysudoku(size):
    return creatematrix(size, size, size)


def printmatrix(matrix):
    """
    Prints a n x n sudoku matrix with grid lines
    """
    size = len(matrix)
    blocksize = int(math.sqrt(size))
    lookup = "0123456789abcdefghijklmnopqrstuvwxyz"
    output = ""
    row_num = 0
    output += "-" * (1 + (blocksize*3+3)*blocksize) + "\n"
    for row in matrix:
        output += "|  "
        col_num = 0
        for value in row:
            if value >= size:
                value = "-"
            elif value < len(lookup):
                value = lookup[value]
            output += str(value) + "  "
            if col_num % blocksize == blocksize-1:
                output += "|  "
            col_num += 1
        output += "\n"
        if (row_num % blocksize == blocksize-1):
            output += "-" * (1 + (blocksize*3+3)*blocksize) + "\n"
        row_num += 1
    print(output)


def checkrows(matrix):
    """
    Checks if each row contains each value only once
    """
    size = len(matrix)
    row_num = 0
    for row in matrix:
        numbercontained = [False for x in range(size)]
        for value in row:
            # if placeholder, ignore it
            if value in range(size):
                if numbercontained[value]:
                    return False
                else:
                    numbercontained[value] = True
        row_num += 1
    return True


def checkcols(matrix):
    """
    Checks if each column contains each value only once
    """
    size = len(matrix)
    for col_num in range(size):
        numbercontained = [False for x in range(size)]
        for row_num in range(size):
            value = matrix[row_num][col_num]
            # if placeholder, ignore it
            if value in range(size):
                if numbercontained[value]:
                    return False
                else:
                    numbercontained[value] = True
    return True


def checkblocks(matrix):
    """
    Checks if each block contains each value only once
    """
    size = len(matrix)
    blocksize = int(math.sqrt(size))
    row_num = 0
    col_num = 0
    for block_num in range(size):
        numbercontained = [False for x in range(size)]
        for value_num in range(size):
            value = matrix[row_num][col_num]
            # if placeholder, ignore it
            if value in range(size):
                if numbercontained[value]:
                    return False
                else:
                    numbercontained[value] = True
            col_num += 1
            if col_num % blocksize == 0:
                col_num -= blocksize
                row_num += 1
        col_num += blocksize
        row_num -= blocksize
        if col_num == size:
            col_num = 0
            row_num += blocksize
    return True


def checksudoku(matrix):
    """
    Checks if matrix contains a valid (partially) filled out sudoku
    """
    if checkrows(matrix):
        if checkcols(matrix):
            if checkblocks(matrix):
                return True
    return False


def trysudoku(matrix, row, col, value):
    """
    Tries to insert value to matrix[row][col] and
    checks if it is a valid sudoku. If yes, the
    new matrix is returned, if not the change is
    undone and the old matrix is returned.
    """
    oldvalue = matrix[row][col]
    matrix[row][col] = value
    if checksudoku(matrix):
        # keep change
        return matrix, True
    else:
        # undo change
        matrix[row][col] = oldvalue
        return matrix, False


def getrandomarray(size):
    array = [x for x in range(size)]
    random.shuffle(array)
    return array


def recurse(matrix, row, col, depth):
    size = len(matrix)

    col_new = col + 1
    row_new = row
    if col_new == size:
        col_new = 0
        row_new = row + 1

    # randomize value order
    array = getrandomarray(size)
    for value in array:
        # test if valid
        matrix, success = trysudoku(matrix, row, col, value)
        if success:
            # check if sudoku is filled out completely
            if row == size - 1 and col == size - 1:
                return matrix, True
            else:
                # if not finished, recurse deeper
                matrix, finished = recurse(
                    matrix, row_new, col_new, depth+1)
                if finished:
                    # pass on result
                    return matrix, True

    # no success? return and try other path
    return matrix, False


def generatesudoku(size):
    """
    Generates a fully filled out sudoku with
    the specified size.

    Tree search with randomized value choice.
    """
    # check if size is square number
    if not (math.sqrt(size)).is_integer():
        print("{0} is not a square number!".format(size))
        sys.exit(1)

    matrix = createemptysudoku(size)
    matrix, finished = recurse(matrix, 0, 0, 0)
    return matrix, finished


def generategaps(matrix, gap_probability):
    size = len(matrix)
    for row in range(size):
        for col in range(size):
            if random.uniform(0, 1) < gap_probability:
                matrix[row][col] = size
    return matrix


def main(size=9, gap_probability=0.5, max_tries=50):

    if len(sys.argv) == 4:
        size = int(sys.argv[1])
        gap_probability = float(sys.argv[2])
        max_tries = int(sys.argv[3])
    else:
        print("possible arguments:")
        print("- sudoku size (try 4, 9, 16, 25)")
        print("- gap probability in [0, 1]")
        print("- max number of tries")

    print("\nsudoku size: ", size)

    finished = False
    tries = 1

    while not finished and tries <= max_tries:
        result, finished = generatesudoku(size)
        print("try {0} of {1}, finished: {2}".format(
            tries, max_tries, finished))

        if finished or tries == max_tries:
            printmatrix(result)
            print("adding gaps with probability", gap_probability)
            matrix = generategaps(result, gap_probability)
            printmatrix(matrix)

        tries += 1

    return result


if __name__ == "__main__":
    main()
