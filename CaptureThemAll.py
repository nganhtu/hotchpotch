from icecream import ic


knight = (0, 0)
queen = (1, 6)
rook = (6, 1)


def get_available_moves(knight):
    available_moves = []
    x, y = knight
    for i in range(2):
        for ii in range(2):
            for iii in range(2):
                for iv in range(2):
                    new_x = x + (i + 1) * (-1) ** ii
                    new_y = y + (iii + 1) * (-1) ** iv
                    if 0 <= new_x < 8 and 0 <= new_y < 8 and abs(new_x - x) + abs(new_y - y) == 3:
                        available_moves.append((new_x, new_y))
    return available_moves

ic(get_available_moves(queen))


def bfs(start, end):
    passed = []
    queue = [[start, 0]]
    while len(queue) > 0:
        current, step = queue.pop(0)
        passed.append(current)
        if current == end:
            return step
        available_moves = get_available_moves(current)
        for move in available_moves:
            if move is not passed:
                queue.append([move, step + 1])
    return -1

ic(bfs(queen, rook))
result = min(bfs(knight, queen), bfs(knight, rook)) + bfs(queen, rook)
ic(result)
