a = [3, 44, 38, 5, 47, 151, 36, 26, 27, 2, 46, 61, 19, 50, 50, 48]


def bottom_up_heapify(pos):
    if pos == -1:
        return
    parent = (pos - 1) // 2
    if a[pos] > a[parent]:
        a[pos], a[parent] = a[parent], a[pos]
        bottom_up_heapify(parent)


def top_down_heapify(pos, end):
    left = pos * 2 + 1
    right = pos * 2 + 2
    max = a[pos]
    tmp = pos
    if left < end and max < a[left]:
        max = a[left]
        tmp = left
    if right < end and max < a[right]:
        max = a[right]
        tmp = right
    if tmp != pos:
        a[pos], a[tmp] = a[tmp], a[pos]
        top_down_heapify(tmp, end)


def build_heap():
    for i in range(len(a) - 1, -1, -1):
        top_down_heapify(i, len(a))


def print_max():
    # a is a heap
    print(a[0])


def add(new_elm):
    # a is a heap
    a.append(new_elm)
    bottom_up_heapify(len(a) - 1)


def change(index, new_value):
    old_value = a[index]
    a[index] = new_value
    if new_value > old_value:
        bottom_up_heapify(index)
    elif new_value < old_value:
        top_down_heapify(index, len(a))


def delete_root():
    # a is a heap
    a[0], a[len(a) - 1] = a[len(a) - 1], a[0]
    a.pop(len(a) - 1)
    top_down_heapify(0, len(a))


print(a)
build_heap()
print(a)
print_max()
add(13)
print(a)
change(1, 4)
print(a)
delete_root()
print(a)
