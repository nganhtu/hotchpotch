from icecream import ic


origin = "aaaa"
finality = "zzzz"
honkai = (("z", "a", "a", "a"), ("a", "z", "a", "a"), ("a", "a", "z", "a"), ("a", "a", "a", "z"),
          ("a", "z", "z", "z"), ("z", "a", "z", "z"), ("z", "z", "a", "z"), ("z", "z", "z", "a"))


def isValid(str):
    for strict in honkai:
        for i in range(4):
            if strict[i].find(str[i]) == -1:
                break
            if i == 3:
                return False
    return True


def get_adjacent(str):
    res = []
    for i in range(4):
        for ii in range(2):
            res.append("".join((str[0:i],
                                chr(ord("a") + (ord(str[i]) - ord("a") + (-1) ** ii) % 26),
                                str[i + 1:4])))
    return res


def count_step():
    queue = [[origin, 0]]
    passed = []
    while len(queue) > 0:
        str, step = queue.pop(0)
        ic('checking~', len(passed), step, str)
        if str == finality:
            return step
        passed.append(str)
        adjacents = get_adjacent(str)
        for adj in adjacents:
            if adj not in passed and isValid(adj):
                queue.append([adj, step + 1])


ic(count_step())
