# Cho một xâu S, độ dài n <= 1000 kí tự.
# Tìm palindrome dài nhất là xâu con của S (xâu con là một dãy các kí tự liên tiếp)

text = input().strip()

# Cách 1: quy hoạch động (O(n^2))

# Tạo mảng 2 chiều F kích thước n * n.
# Định nghĩa: F[i][j] = is_palindrome(s[i:j + 1])

# Ta có công thức quy hoạch động:
# F[i][i - 1] = True: xâu 0 kí tự luôn đối xứng;
# F[i][i] = True: xâu 1 kí tự luôn đối xứng;
# Nếu s[i] == s[j] thì F[i + 1][j - 1] == F[i][j];
# Nếu s[i] != s[j] thì F[i][j] = False.


# Cách 2: cũng O(n^2) nhưng dễ cài đặt hơn quy hoạch động :)
# Ý tưởng: mọi xâu con độ dài 0 hoặc 1 đều là palindrome,
# nên ta sẽ "mở rộng" từng palindrome đó ra hết cỡ rồi trả về độ dài lớn nhất.


def expand(text, left, right):
    while left > 0 and right < len(text) - 1 and text[left - 1] == text[right + 1]:
        left -= 1
        right += 1
    return right - left + 1


res = 0

# even-length substrings
for i in range(1, len(text)):
    res = max(res, expand(text, i, i - 1))

# odd-length substrings
for i in range(len(text)):
    res = max(res, expand(text, i, i))

print(res)

# Cách 2 nhanh hơn cách 1 gấp một hằng số ( hình như là 4).
# Có thể thấy không phải lúc nào QHĐ cũng tốt hơn duyệt.
