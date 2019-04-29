# https://www.codewars.com/kata/sudoku-solution-validator/train/python
from functools import reduce


def validSolution(board):
    s = sum(range(1, 10))
    if reduce(lambda a, b: a + b, [r.count(0) for r in board]) > 0:
        return False
    if [sum(r) for r in board] != [s] * 9:
        return False
    for i in range(9):
        if sum(col(board, i)) != s:
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            print("%d %d" % (i, j))
            if sum(palace(board, i, j)) != s:
                # return False
                pass
    return True


def col(board, i):
    return [r[i] for r in board]


def palace(puz, i, j):
    matrix = [r[j : j + 3] for r in puz[i : i + 3]]
    return [i for item in matrix for i in item]


p = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

if __name__ == "__main__":
    print(validSolution(p))
