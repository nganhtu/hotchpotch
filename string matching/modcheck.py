pattern = input()


pi = [0] * len(pattern)
k = 0
for i in range(1, len(pattern)):
    while k > 0 and pattern[k] != pattern[i]:
        k = pi[k - 1]
    if pattern[k] == pattern[i]:
        k += 1
    pi[i] = k


print(pi)
