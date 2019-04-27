from functools import reduce

# https://www.codewars.com/kata/sudoku-solver/train/python


def sudoku(puzzle):
    while True:
        puzzle2 = [[i for i in row] for row in puzzle]
        reduce_current(puzzle)
        if puzzle2 == puzzle:
            break
    return puzzle


def reduce_current(puzzle):
    old_puzzle = [[i for i in row] for row in puzzle]
    for i in range(9):
        row = puzzle[i]
        # print(row)
        for j in range(9):
            val = row[j]
            if not val:
                c = candidate(puzzle, i, j)
                # print('(%d, %d) -> %r'%(i,j,c))
                if len(c) == 1:
                    puzzle[i][j] = c[0]
    if puzzle != old_puzzle:
        print('chanded')
    return puzzle


def candidate(puz, i, j):
    rowi = puz[i]
    columnj = [r[j] for r in puz]
    palaceij = palace(puz, [i//3, j//3])
    exists = set(reduce(lambda x, y: x+y, [rowi, columnj, palaceij]))
    return list(set(range(1, 10)) - exists)


def palace(puz, coor):
    ret = []
    i, j = coor
    matrix = [r[j*3:j*3+3] for r in puz[i*3:i*3+3]]
    return [i for item in matrix for i in item]


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

my = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
      [6, 7, 2, 1, 9, 5, 3, 4, 8],
      [1, 9, 8, 3, 4, 2, 5, 6, 7],
      [8, 5, 9, 7, 6, 1, 4, 2, 3],
      [4, 2, 6, 8, 5, 3, 7, 9, 1],
      [7, 1, 3, 9, 2, 4, 8, 5, 6],
      [9, 6, 1, 5, 3, 7, 2, 8, 4],
      [2, 8, 7, 4, 1, 9, 6, 3, 5],
      [3, 4, 5, 2, 8, 6, 1, 7, 9]]


def cnt(puz):
    return reduce(lambda i, j: i+j, map(lambda r: r.count(0), puz))


if __name__ == "__main__":
    # sudoku(puzzle)
    print(sudoku(puzzle))
    # print(candidate(puzzle, 0, 0))
    # for i in range(9):
    #     for j in range(i,9):
    # print(cnt(puzzle))
    # print(cnt(milestone1))
