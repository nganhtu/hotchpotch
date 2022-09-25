import time
import random


a = [3, 44, 38, 5, 47, 151, 36, 26, 27, 2, 46, 61, 19, 50, 50, 48]


def execution_time(f):
    start_time = time.time()
    f()
    print('Execution time is {} seconds.'.format(time.time() - start_time))


def bubble_sort():
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]


def insertion_sort():
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j - 1] > a[i]:
            j -= 1
        tmp = a[i]
        for k in range(i, j, -1):
            a[k] = a[k - 1]
        a[j] = tmp


def _merge_sort(a, left, right):
    if left < right:
        mid = (left + right) // 2
        _merge_sort(a, left, mid)
        _merge_sort(a, mid + 1, right)
        tmp = [0] * len(a)
        curr, i, j = left, left, mid + 1
        while i <= mid or j <= right:
            if i > mid:
                tmp[curr] = a[j]
                curr += 1
                j += 1
            elif j > right:
                tmp[curr] = a[i]
                curr += 1
                i += 1
            elif a[i] < a[j]:
                tmp[curr] = a[i]
                curr += 1
                i += 1
            else:
                tmp[curr] = a[j]
                curr += 1
                j += 1
        # print(tmp)    # uncomment this line to see a pretty visualization
        for i in range(left, right + 1):
            a[i] = tmp[i]


def merge_sort():
    _merge_sort(a, 0, len(a) - 1)


def heapify(root, end):
    left = root * 2 + 1
    right = root * 2 + 2
    max = a[root]
    pos = root
    if left < end and max < a[left]:
        max = a[left]
        pos = left
    if right < end and max < a[right]:
        max = a[right]
        pos = right
    if pos != root:
        a[root], a[pos] = a[pos], a[root]
        heapify(pos, end)


def heap_sort():
    for i in range(len(a) - 1, -1, -1):
        heapify(i, len(a))
    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(0, i - 1)


def _quick_sort(a, left, right):
    i, j = left, right
    pivot = a[random.randint(left, right)]
    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if j > left:
        _quick_sort(a, left, j)
    if i < right:
        _quick_sort(a, i, right)


def quick_sort():
    _quick_sort(a, 0, len(a) - 1)


def radix_sort():
    BASE = 13
    exp = 1
    while BASE ** exp <= max(a) * BASE:
        tmp = [[] for _ in range(BASE)]
        for i in a:
            tmp[i % (BASE ** exp) // (BASE ** (exp - 1))].append(i)
        curr = 0
        for i in tmp:
            for j in i:
                a[curr] = j
                curr += 1
        exp += 1


print(a)
execution_time(quick_sort)
print(a)
