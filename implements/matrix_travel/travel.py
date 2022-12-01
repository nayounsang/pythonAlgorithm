# init
X = 500
Y = 500


def vaild(x, y):
    if 0 <= x < X and 0 <= y < Y:
        '''
        if board[y][x] == DONT:
            return False
        '''
        return True
    return False


def four_direct(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def eight_direct(x, y):
    return [(x + 1, y), (x + 1, y - 1), (x + 1, y + 1), (x, y + 1), (x, y - 1), (x - 1, y), (x - 1, y - 1),
            (x - 1, y + 1)]


four = [(0, 1), (1, 0), (0, -1), (-1, 0)]
eight = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
