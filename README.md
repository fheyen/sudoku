# sudoku

[github.com/fheyen/sudoku/](https://github.com/fheyen/sudoku/)

A Sudoku generator written in Python. Able to generate sudokus in various sizes (square numbers only). Tested with 1, 4, 9, 16 and 25. 36 works if `recursion_limit` is set to a value of 2000. Large sudokus may take a lot of time to generate.

## Usage

```bash
python .\sudoku.py size gap_probability max_tries recursion_limit
```

Example:

```bash
python .\sudoku.py 16 0.5 50 1000
```

Output for example (may vary due to randomness):

```
PS R:\dev\sudoku> python .\sudoku.py 16 0.5

sudoku size:  16
-------------------------------------------------------------
|  a  1  c  6  |  8  2  0  e  |  5  9  7  4  |  b  f  d  3  |
|  f  5  9  4  |  d  6  7  a  |  e  3  8  b  |  1  c  0  2  |
|  e  b  2  3  |  c  f  5  9  |  1  a  d  0  |  8  7  4  6  |
|  0  8  d  7  |  4  1  3  b  |  6  2  c  f  |  a  5  9  e  |
-------------------------------------------------------------
|  3  0  5  a  |  1  e  b  8  |  9  7  6  c  |  f  4  2  d  |
|  1  2  b  e  |  3  c  a  6  |  8  f  4  d  |  5  0  7  9  |
|  6  9  8  d  |  7  0  4  f  |  3  1  2  5  |  c  e  a  b  |
|  c  7  4  f  |  5  9  d  2  |  b  0  a  e  |  6  3  8  1  |
-------------------------------------------------------------
|  7  6  3  5  |  a  b  8  4  |  d  e  0  2  |  9  1  f  c  |
|  9  e  f  2  |  6  d  c  7  |  4  5  3  1  |  0  8  b  a  |
|  4  c  0  8  |  f  3  9  1  |  a  6  b  7  |  d  2  e  5  |
|  d  a  1  b  |  2  5  e  0  |  c  8  f  9  |  4  6  3  7  |
-------------------------------------------------------------
|  8  f  a  9  |  0  7  6  c  |  2  b  1  3  |  e  d  5  4  |
|  5  d  7  c  |  9  8  1  3  |  f  4  e  a  |  2  b  6  0  |
|  2  4  e  0  |  b  a  f  d  |  7  c  5  6  |  3  9  1  8  |
|  b  3  6  1  |  e  4  2  5  |  0  d  9  8  |  7  a  c  f  |
-------------------------------------------------------------

adding gaps with probability 0.5
-------------------------------------------------------------
|  -  -  -  -  |  -  -  -  e  |  5  9  7  4  |  -  -  d  3  |
|  f  -  -  4  |  d  6  7  a  |  -  3  -  -  |  1  -  -  2  |
|  e  -  2  3  |  c  f  5  -  |  1  a  d  0  |  8  -  4  -  |
|  0  -  -  7  |  4  -  -  -  |  -  2  c  -  |  a  -  -  -  |
-------------------------------------------------------------
|  3  0  -  -  |  -  e  -  8  |  -  -  -  -  |  f  4  -  d  |
|  1  2  -  -  |  3  -  -  6  |  -  -  -  -  |  5  -  7  -  |
|  6  9  8  d  |  7  -  -  -  |  3  -  2  -  |  -  -  a  b  |
|  -  -  -  f  |  5  -  -  -  |  -  -  a  -  |  -  3  -  1  |
-------------------------------------------------------------
|  7  -  -  5  |  -  -  8  -  |  d  e  0  2  |  9  1  f  -  |
|  9  e  f  2  |  6  d  -  -  |  -  -  3  1  |  -  8  b  -  |
|  4  c  -  8  |  -  -  -  1  |  a  -  -  7  |  -  -  -  5  |
|  -  a  1  -  |  -  -  -  0  |  -  -  f  9  |  4  -  3  -  |
-------------------------------------------------------------
|  8  -  -  9  |  0  -  6  -  |  2  b  -  3  |  e  d  -  -  |
|  5  -  7  c  |  -  8  -  -  |  f  4  -  a  |  -  -  -  0  |
|  -  4  -  -  |  -  -  -  -  |  -  c  -  -  |  -  9  1  -  |
|  -  3  -  1  |  -  4  2  -  |  -  d  9  -  |  7  -  c  -  |
-------------------------------------------------------------
```
