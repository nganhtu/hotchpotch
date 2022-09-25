# https://vnoi.info/wiki/translate/wcipeg/kmp.md

# Thuật toán Knuth-Morris-Pratt

# Ý tưởng của thuật toán xuất phát từ nhu cầu khắc phục nhược điểm của brute force:
# Khi so sánh và nhận thấy pattern[i] != text[j],
# chương trình đã tốn tài nguyên để có được thông tin pattern[0:i] == text[j - i:j]
# nhưng brute force không sử dụng đến thông tin này.
# Ý tưởng của thuật toán KMP là tìm trước vị trí lặp lại
# của tất cả các tiền tố của pattern để tận dụng thông tin đã nói trên.

text = input().strip()
pattern = input().strip()

# π của một xâu là độ dài xâu con dài nhất của xâu đó thỏa mãn
# vừa là tiền tố thực, vừa là hậu tố thực của xâu gốc.
# VD: π['asasa'] = 3


def find_pi(s):
    for i in range(len(s) - 1, 0, -1):
        if s[:i] == s[len(s) - i:len(s)]:
            return i
    return 0

# Mảng pi của một xâu là mảng chứa các π của tất cả các tiền tố của xâu đó:
# pi[i] = π[pattern[0:i + 1]]                     với i in range(len(pattern)).
# VD: pi['asasa'] = [0, 0, 1, 2, 3]


pi = [0] * len(pattern)
for i in range(len(pattern)):
    pi[i] = find_pi(pattern[:i + 1])


# Lưu ý code trên có độ phức tạp O(n^2).
# Code có độ phức tạp O(n):
pi = [0] * len(pattern)
k = 0
for i in range(1, len(pattern)):
    while k > 0 and pattern[k] != pattern[i]:
        k = pi[k - 1]
    if pattern[k] == pattern[i]:
        k += 1
    pi[i] = k
# Đoạn code trên sử dụng quy hoạch động để tính pi[i] dựa vào các pi[:i] trước đó.
# Sau khi chạy xong vòng lặp while,
# chỉ số k nằm ở 0 hoặc cuối tiền tố dài nhất cũng là hậu tố thực của pattern[:i + 1].


res = []
i, j = 0, 0
while i < len(text):
    if text[i] == pattern[j]:
        if j < len(pattern) - 1:
            i += 1
            j += 1
        else:
            res.append(i - len(pattern) + 1)
            if j > 0:
                j = pi[j - 1]
            else:
                i += 1
    else:
        if j > 0:
            j = pi[j - 1]
        else:
            i += 1
print(res)
