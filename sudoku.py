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
import time


def create2dimarray(w, h, initialval):
    sudoku = [[initialval for x in range(w)] for y in range(h)]
    return sudoku


def createemptysudoku(size):
    return create2dimarray(size, size, size)


def printsudoku(sudoku):
    """
    Prints a n x n sudoku sudoku with grid lines
    """
    size = len(sudoku)
    blocksize = int(math.sqrt(size))
    lookup = "0123456789abcdefghijklmnopqrstuvwxyz"
    output = ""
    row_num = 0
    output += "-" * (1 + (blocksize*3+3)*blocksize) + "\n"
    for row in sudoku:
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


def checkrows(sudoku):
    """
    Checks if each row contains each value only once
    """
    size = len(sudoku)
    row_num = 0
    for row in sudoku:
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


def checkcols(sudoku):
    """
    Checks if each column contains each value only once
    """
    size = len(sudoku)
    for col_num in range(size):
        numbercontained = [False for x in range(size)]
        for row_num in range(size):
            value = sudoku[row_num][col_num]
            # if placeholder, ignore it
            if value in range(size):
                if numbercontained[value]:
                    return False
                else:
                    numbercontained[value] = True
    return True


def checkblocks(sudoku):
    """
    Checks if each block contains each value only once
    """
    size = len(sudoku)
    blocksize = int(math.sqrt(size))
    row_num = 0
    col_num = 0
    for block_num in range(size):
        numbercontained = [False for x in range(size)]
        for value_num in range(size):
            value = sudoku[row_num][col_num]
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


def checksudoku(sudoku):
    """
    Checks if sudoku contains a valid (partially) filled out sudoku
    """
    if checkrows(sudoku):
        if checkcols(sudoku):
            if checkblocks(sudoku):
                return True
    return False


def trysudoku(sudoku, row, col, value):
    """
    Tries to insert value to sudoku[row][col] and
    checks if it is a valid sudoku. If yes, the
    new sudoku is returned, if not the change is
    undone and the old sudoku is returned.
    """
    oldvalue = sudoku[row][col]
    sudoku[row][col] = value
    if checksudoku(sudoku):
        # keep change
        return sudoku, True
    else:
        # undo change
        sudoku[row][col] = oldvalue
        return sudoku, False


def getrandomarray(size):
    array = [x for x in range(size)]
    random.shuffle(array)
    return array


def getnextfield(row, col, size):
    """
    Returns coordinates of next field
    """
    col = col + 1
    if col >= size:
        col = 0
        row = row + 1
    return row, col


def getpreviousfield(row, col, size):
    """
    Returns coordinates of previous field
    """
    col = col - 1
    if col <= -1:
        col = size - 1
        row = row - 1
    return row, col


def recurse(matrix, row, col):
    """
    Generates a fully filled out sudoku with
    the specified size.
    Tree search with randomized value choice.
    """
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
                    matrix, row_new, col_new)
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
    matrix, finished = recurse(matrix, 0, 0)
    return matrix, finished


def generatesudoku_iterative(size):
    """
    Generates a fully filled out sudoku with
    the specified size.

    Tree search with randomized value choice.
    """
    sudoku = createemptysudoku(size)
    # keep track of shuffled values current index
    # for each field in the sudoku
    values = create2dimarray(size, size, None)
    indices = create2dimarray(size, size, 0)

    # only create shuffled values once
    for r in range(size):
        for c in range(size):
            values[r][c] = getrandomarray(size)

    # fill out sudoku field by field and
    # go back one field if failed
    row = 0
    col = 0
    num_tests = 0
    start = time.time()
    lasttimeprinted = start
    while(True):
        index = indices[row][col]
        if index >= size:
            # all values failed, reset current field
            # and go back to previous field
            sudoku[row][col] = size
            row, col = getpreviousfield(row, col, size)
            # check if failed completely
            if row <= -1:
                return sudoku, False
            # increase index of previous field
            indices[row][col] += 1
        else:
            # test next value
            num_tests += 1
            value = values[row][col][index]
            sudoku, success = trysudoku(sudoku, row, col, value)
            if success:
                # go to next field
                row, col = getnextfield(row, col, size)
                # check if finished
                if row >= size:
                    return sudoku, True
                else:
                    # reset index of next field
                    indices[row][col] = 0
            else:
                # increase index of current field
                indices[row][col] += 1

        # show performance message every 5 seconds
        currenttime = time.time()
        timespent = currenttime - start
        if currenttime - lasttimeprinted > 5:
            print("time: {:.1f}s, number of tests: {:d}, tests per second: {:.1f}       ".format(
                timespent, num_tests, num_tests / timespent), end="\r")
            lasttimeprinted = currenttime

    return sudoku, False


def generategaps(sudoku, gap_probability):
    """
    Adds gaps to a filled out sudoku
    """
    size = len(sudoku)
    for row in range(size):
        for col in range(size):
            if random.uniform(0, 1) < gap_probability:
                sudoku[row][col] = size
    return sudoku


def solvesudoku(sudoku):
    """
    Solves a partially filled out sudoku
    """
    # TODO:
    # for each field, get all possible values


def main(size=9, gap_probability=0.5):
    """
    Reads console arguments and runs generator
    """
    # read arguments
    if len(sys.argv) == 3:
        size = int(sys.argv[1])
        gap_probability = float(sys.argv[2])
    else:
        print("possible arguments:")
        print("- sudoku size (try 1, 4, 9, 16 or 25)")
        print("- gap probability in [0.0, 1.0]")

    # check if size is square number
    if not (math.sqrt(size)).is_integer():
        print("{0} is not a square number!".format(size))
        sys.exit(1)

    print("\nsudoku size: ", size)

    # try until finished or too many tries
    result, finished = generatesudoku_iterative(size)

    if finished:
        printsudoku(result)
        if finished:
            print("adding gaps with probability", gap_probability)
            sudoku = generategaps(result, gap_probability)
            printsudoku(sudoku)

    return result


if __name__ == "__main__":
    main()
