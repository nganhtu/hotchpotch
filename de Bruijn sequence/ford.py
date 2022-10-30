n = 5
length = 2 ** n
sequence = [0] * length
for i in range(n, length):
    sequence[i] = 1
    for j in range(0, i - n + 1):
        if sequence[i - n + 1:i + 1] == sequence[j:j + n]:
            sequence[i] = 0
print(sequence)
