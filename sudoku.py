"""
Sudoku generator
"""

# TODO: infer size from matrix instead of param

# use __future__ to provide compatibility with python 3
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import random


verbose = False


def print_verbose(to_print):
    global verbose
    if verbose:
        print(to_print)


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
                    print_verbose(
                        "Number {0} occurs more than once in row {1}!".format(value, row_num))
                    return False
                else:
                    numbercontained[value] = True
        row_num += 1
    print_verbose("rows are fine")
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
                    print_verbose(
                        "Number {0} occurs more than once in col {1}!".format(value, col_num))
                    return False
                else:
                    numbercontained[value] = True
    print_verbose("cols are fine")
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
                    print_verbose(
                        "Number {0} occurs more than once in block {1}!".format(value, block_num))
                    return False
                else:
                    numbercontained[value] = True
            col_num += 1
            if col_num % blocksize == 0:
                col_num -= 4
                row_num += 1
        col_num += blocksize
        row_num -= blocksize
        if col_num == size:
            col_num = 0
            row_num += blocksize
    print_verbose("blocks are fine")
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


def generatesudoku(size):
    """
    Generates a fully filled out sudoku with
    the specified size
    """
    # check if size is square number
    if not (math.sqrt(size)).is_integer():
        print("{0} is not a square number!".format(size))
        return

    matrix = creatematrix(size, size, size)
    total_tries = 0
    for row in range(size):
        for col in range(size):
            try_num = 1
            for value in range(size):
                matrix, success = trysudoku(matrix, row, col, value)
                if success:
                    if verbose:
                        print("success after {0} tries:".format(try_num))
                        printmatrixhex(matrix)
                    total_tries += try_num
                    # no further tries required
                    break
                else:
                    try_num += 1
    return matrix


def recurse(matrix, row, col, depth):
    size = len(matrix)

    col_new = col + 1
    row_new = row
    if col_new == size:
        col_new = 0
        row_new = row + 1

    # randomize value
    array = getrandomarray(size)

    for value in array:
        # test if valid
        matrix, success = trysudoku(matrix, row, col, value)
        if success:
            # check if sudoku is filled out completely
            if row == size - 1 and col == size - 1:
                print("finished!")
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


def generatesudoku_randomized_tree(size):
    """
    Generates a fully filled out sudoku with
    the specified size.

    Tree search with randomized value choice.
    """
    # check if size is square number
    if not (math.sqrt(size)).is_integer():
        print("{0} is not a square number!".format(size))
        return

    matrix = creatematrix(size, size, size)
    matrix, finished = recurse(matrix, 0, 0, 0)
    return matrix, finished


def main():
    global verbose
    verbose = False

    result, finished = generatesudoku_randomized_tree(16)
    print("finished: ", finished)
    printmatrixhex(result)


if __name__ == "__main__":
    main()
