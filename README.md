# sudoku

A Sudoku generator written in Python. Able to generate sudokus in various sizes (square numbers only). Tested with 1, 4, 9, 16 and 25.

## Usage

```bash
python .\sudoku.py size gap_probability max_tries
```

Example:

```bash
python .\sudoku.py 16 0.5 50
```

Output for example (may vary due to randomness):

```
sudoku size:  16
try 1 of 50, finished: False
try 2 of 50, finished: False
try 3 of 50, finished: False
try 4 of 50, finished: False
try 5 of 50, finished: False
try 6 of 50, finished: False
try 7 of 50, finished: False
try 8 of 50, finished: False
try 9 of 50, finished: False
try 10 of 50, finished: True
-------------------------------------------------------------
|  8  f  9  5  |  6  d  3  c  |  a  b  4  1  |  e  7  0  2  |
|  b  6  2  4  |  9  8  5  e  |  f  c  7  0  |  a  1  3  d  |
|  e  d  a  1  |  0  4  2  7  |  6  8  9  3  |  c  b  f  5  |
|  0  7  c  3  |  f  1  b  a  |  d  e  2  5  |  9  6  8  4  |
-------------------------------------------------------------
|  4  a  b  6  |  7  2  e  1  |  0  3  f  c  |  5  9  d  8  |
|  2  3  8  0  |  b  f  c  5  |  1  9  6  d  |  4  e  a  7  |
|  7  e  d  9  |  a  3  6  0  |  8  4  5  2  |  1  f  c  b  |
|  5  c  1  f  |  d  9  4  8  |  7  a  e  b  |  2  3  6  0  |
-------------------------------------------------------------
|  9  0  6  7  |  e  b  d  f  |  c  5  3  a  |  8  4  2  1  |
|  f  4  3  d  |  1  0  a  9  |  e  2  b  8  |  6  5  7  c  |
|  c  b  e  8  |  3  5  7  2  |  4  0  1  6  |  f  d  9  a  |
|  1  2  5  a  |  4  c  8  6  |  9  f  d  7  |  3  0  b  e  |
-------------------------------------------------------------
|  d  9  7  c  |  8  a  f  3  |  5  1  0  e  |  b  2  4  6  |
|  3  1  f  b  |  c  e  0  d  |  2  6  8  4  |  7  a  5  9  |
|  6  8  4  2  |  5  7  1  b  |  3  d  a  9  |  0  c  e  f  |
|  a  5  0  e  |  2  6  9  4  |  b  7  c  f  |  d  8  1  3  |
-------------------------------------------------------------

adding gaps with probability 0.5
-------------------------------------------------------------
|  -  f  -  -  |  6  d  -  -  |  -  b  -  -  |  -  -  -  -  |
|  -  6  2  -  |  9  8  5  e  |  f  c  7  0  |  -  1  -  d  |
|  e  -  -  -  |  0  4  2  7  |  6  -  9  3  |  -  -  -  5  |
|  -  -  -  3  |  -  -  b  -  |  -  -  -  5  |  -  6  -  -  |
-------------------------------------------------------------
|  4  a  -  -  |  -  2  -  -  |  0  3  -  -  |  5  9  -  8  |
|  2  -  8  -  |  -  f  c  -  |  1  9  6  d  |  4  -  -  -  |
|  -  e  d  -  |  -  -  6  -  |  -  4  5  -  |  -  -  c  b  |
|  5  -  -  f  |  -  9  4  -  |  -  -  e  -  |  -  3  6  0  |
-------------------------------------------------------------
|  -  0  -  7  |  e  -  -  f  |  c  -  -  a  |  8  -  2  1  |
|  f  4  3  -  |  1  -  -  9  |  -  -  b  -  |  -  -  7  -  |
|  c  b  -  8  |  -  5  -  2  |  -  0  1  6  |  -  d  -  -  |
|  1  2  5  -  |  4  c  8  -  |  9  f  -  7  |  -  -  -  e  |
-------------------------------------------------------------
|  d  -  -  c  |  -  -  f  3  |  -  1  -  e  |  -  2  -  -  |
|  -  1  f  -  |  -  e  0  d  |  2  6  -  -  |  -  -  -  9  |
|  6  8  4  -  |  -  -  -  -  |  -  d  -  -  |  -  c  -  f  |
|  -  -  0  -  |  -  -  9  -  |  b  7  c  f  |  -  8  -  -  |
-------------------------------------------------------------
```
