from functools import reduce

# https://www.codewars.com/kata/sudoku-solver/train/python


def solve(puzzle):
    print(puzzle)
    stack = []
    index = 0
    should_back = False
    puzzle_copy = copy(puzzle)
    while True:
        deep = 0
        if should_back:
            should_back = False
            index, deep, puzzle_copy = stack.pop()
            deep += 1

        old = copy(puzzle_copy)
        stack.append([index, deep, old])
        pending = get_pending(puzzle_copy)
        coors = sorted(pending.keys())
        coor = coors[0]
        candidators = pending[coor]
        success = False
        while deep < len(candidators):
            candidator = candidators[deep]
            i, j = coor
            puzzle_copy[i][j] = candidator
            try:
                attampt = sudoku(puzzle_copy)
                # print(attampt)
                if attampt and finish(attampt):
                    puzzle_copy = attampt
                    success = True
                    break
                else:
                    break
            except:
                deep += 1
                if deep == len(candidators):
                    break
                else:
                    i, d, p = stack.pop()
                    stack.append([i, deep, p])
        if success:
            return puzzle_copy
        if deep >= len(candidators):
            should_back = True
            stack.pop()
            continue
        index += 1


copy = lambda puzzle: [[i for i in row] for row in puzzle]


def reset_puzzle(puzzle, stack):
    new_puzzle = [[i for i in row] for row in puzzle]
    for s in stack:
        index, coor, deep = s
        i, j = coor
        new_puzzle[i][j] = 1345678
    return new_puzzle


def get_pending(puzzle):
    pending = {}
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                candidator = candidate(puzzle, i, j)
                pending[(i, j)] = candidator
    return pending


def sudoku(puzzle):
    old = [[i for i in row] for row in puzzle]
    now = [[i for i in row] for row in puzzle]
    while True:
        last = [[i for i in row] for row in now]
        now = reduce_current(puzzle)
        if last == now:
            break
    return now if now != old else None


def finish(puzzle):
    return reduce(lambda a, b: a + b, map(lambda r: r.count(0), puzzle)) == 0


def reduce_current(puzzle):
    copy = [[i for i in row] for row in puzzle]
    for i in range(9):
        row = copy[i]
        # print(row)
        for j in range(9):
            val = row[j]
            if not val:
                c = candidate(copy, i, j)
                # print('(%d, %d) -> %r'%(i,j,c))
                if len(c) == 1:
                    copy[i][j] = c[0]
                elif len(c) == 0:
                    raise Exception("no answer error")
    # if puzzle != copy:
        # print("chanded")
    return copy if puzzle != copy else puzzle


def candidate(puz, i, j):
    rowi = puz[i]
    columnj = [r[j] for r in puz]
    palaceij = palace(puz, [i // 3, j // 3])
    exists = set(reduce(lambda x, y: x + y, [rowi, columnj, palaceij]))
    return list(set(range(1, 10)) - exists)


def palace(puz, coor):
    ret = []
    i, j = coor
    matrix = [r[j * 3 : j * 3 + 3] for r in puz[i * 3 : i * 3 + 3]]
    return [i for item in matrix for i in item]


problem = [
    [9, 0, 0, 0, 8, 0, 0, 0, 1],
    [0, 0, 0, 4, 0, 6, 0, 0, 0],
    [0, 0, 5, 0, 7, 0, 3, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 4, 0],
    [4, 0, 1, 0, 6, 0, 5, 0, 8],
    [0, 9, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 7, 0, 3, 0, 2, 0, 0],
    [0, 0, 0, 7, 0, 5, 0, 0, 0],
    [1, 0, 0, 0, 4, 0, 0, 0, 7],
]

pending = {
    (7, 8): [9, 3, 4, 6],
    (4, 7): [9, 3, 7],
    (3, 0): [8, 2, 3, 5, 7],
    (2, 8): [9, 2, 4, 6],
    (5, 4): [1, 5],
    (0, 7): [5, 6, 7],
    (1, 6): [8, 9, 7],
    (2, 5): [1, 2, 9],
    (8, 5): [8, 9, 2],
    (0, 3): [2, 3, 5],
    (5, 8): [3, 6],
    (8, 2): [8, 9, 2, 3, 6],
    (1, 2): [8, 2, 3],
    (7, 4): [1, 2, 9],
    (6, 7): [8, 1, 5, 6, 9],
    (3, 3): [1, 2, 3, 5, 8, 9],
    (0, 6): [4, 6, 7],
    (8, 1): [8, 2, 3, 5],
    (7, 6): [8, 1, 4, 6, 9],
    (6, 3): [8, 1, 6, 9],
    (5, 6): [1, 6, 7],
    (7, 2): [2, 3, 4, 6, 8, 9],
    (3, 6): [1, 9, 7],
    (7, 7): [8, 1, 3, 6, 9],
    (8, 6): [8, 9, 6],
    (5, 3): [8, 1, 3, 5],
    (4, 1): [2, 3, 7],
    (1, 1): [8, 1, 2, 3, 7],
    (2, 7): [8, 9, 6],
    (3, 2): [8, 2, 3],
    (5, 0): [8, 3, 5, 7],
    (7, 1): [8, 2, 3, 4],
    (4, 5): [9, 2, 3, 7],
    (5, 5): [8, 1, 3, 4, 7],
    (1, 4): [1, 2, 5, 9],
    (6, 0): [8, 5, 6],
    (2, 3): [1, 2, 9],
    (2, 1): [8, 1, 2, 4],
    (8, 7): [8, 9, 3, 5, 6],
    (1, 0): [8, 2, 3, 7],
    (6, 5): [8, 1, 9],
    (3, 5): [1, 2, 3, 7, 8, 9],
    (0, 1): [2, 3, 4, 7],
    (8, 3): [8, 9, 2, 6],
    (7, 0): [8, 2, 3, 6],
    (6, 8): [9, 4, 5, 6],
    (5, 2): [8, 3],
    (6, 1): [8, 4, 5],
    (3, 8): [9, 3],
    (2, 0): [8, 2, 6],
    (1, 8): [9, 2, 5],
    (4, 3): [9, 2, 3],
    (1, 7): [8, 9, 5, 7],
    (0, 5): [2, 3],
    (3, 4): [1, 2, 5, 9],
    (0, 2): [2, 3, 4, 6],
}

mid = [
    [9, 2, 0, 0, 8, 3, 0, 0, 1],
    [0, 0, 0, 4, 0, 6, 0, 0, 0],
    [0, 0, 5, 0, 7, 0, 3, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 4, 0],
    [4, 0, 1, 0, 6, 0, 5, 0, 8],
    [0, 9, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 7, 0, 3, 0, 2, 0, 0],
    [0, 0, 0, 7, 0, 5, 0, 0, 0],
    [1, 0, 0, 0, 4, 0, 0, 0, 7],
]

solution = [
    [9, 2, 6, 5, 8, 3, 4, 7, 1],
    [7, 1, 3, 4, 2, 6, 9, 8, 5],
    [8, 4, 5, 9, 7, 1, 3, 6, 2],
    [3, 6, 2, 8, 5, 7, 1, 4, 9],
    [4, 7, 1, 2, 6, 9, 5, 3, 8],
    [5, 9, 8, 3, 1, 4, 7, 2, 6],
    [6, 5, 7, 1, 3, 8, 2, 9, 4],
    [2, 8, 4, 7, 9, 5, 6, 1, 3],
    [1, 3, 9, 6, 4, 2, 8, 5, 7],
]

my = [
    [9, 2, 6, 5, 8, 3, 4, 7, 1],
    [7, 1, 3, 4, 2, 6, 9, 8, 5],
    [8, 4, 5, 9, 7, 1, 3, 6, 2],
    [3, 6, 2, 8, 5, 7, 1, 4, 9],
    [4, 7, 1, 2, 6, 9, 5, 3, 8],
    [5, 9, 8, 3, 1, 4, 7, 2, 6],
    [6, 5, 7, 1, 3, 8, 2, 9, 4],
    [2, 8, 4, 7, 9, 5, 6, 1, 3],
    [1, 3, 9, 6, 4, 2, 8, 5, 7],
]

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

my2 = [
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


def cnt(puz):
    return reduce(lambda i, j: i + j, map(lambda r: r.count(0), puz))


if __name__ == "__main__":
    print(solve(puzzle))
    print(solve(problem))
    # print(pending.keys())
    # print(finish(solution))
    # print(solution == my)

