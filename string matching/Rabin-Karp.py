# https://vnoi.info/wiki/algo/string/hash

# Ý tưởng thuật toán:
# Để so sánh 2 xâu, ta đổi 2 xâu ra số tương ứng
# trong hệ cơ số BASE lớn hơn số lượng kí tự có thể xuất hiện.
# 2 xâu bằng nhau <=> 2 số tương ứng bằng nhau.
# Thuật toán này nhanh hơn brute force dựa trên đặc trưng của máy tính:
# so sánh số nhanh hơn so sánh xâu (thời gian O(1) so với O(n)).
# https://en.wikipedia.org/wiki/Digital_comparator

# Để đơn giản, ta đổi số từ hệ cơ số BASE sang hệ thập phân.
# Tuy nhiên số này có thể rất lớn, nên cần so sánh bằng đồng dư thức.

# Khi đó, thuật toán hoạt động dựa trên ngộ nhận sau:
# a ≡ b mod MOD <=> a = b
# Ngộ nhận trên là sai. Thuật toán sử dụng ngộ nhận này nên không chính xác tuyệt đối.
# Để xác suất xảy ra sai sót trên mỗi truy vấn là 1 / MOD,
# ta cần chọn BASE và MOD là số nguyên tố.
# Chứng minh: https://rng-58.blogspot.com/2017/02/hashing-and-probability-of-collision.html

# Độ phức tạp thời gian: O(m + n), không gian: O(m - n).

BASE = 31
MOD = 10 ** 9 + 7

# Nên chọn hệ cơ số 311.
# Đó là số nguyên tố lớn hơn số lượng kí tự trong bảng mã UTF-8.
# Do đó ta cũng không cần phải trừ đi hash của 'a' như hàm dưới đây.


def hash_char(c):
    return ord(c) - ord('a') + 1
    # tuyệt đối lưu ý hash mọi kí tự phải khác 0


def hash_pattern(pattern):
    res = 0
    for c in pattern:
        res = (res * BASE + hash_char(c)) % MOD
    return res


def hash_text(text, len_pattern):
    res = [0] * (len(text) - len_pattern + 1)
    res[0] = hash_pattern(text[:len_pattern])
    for i in range(len(text) - len_pattern):
        # Lưu ý rằng với một số ngôn ngữ như C++,
        # phép tính đồng dư số âm có thể dẫn đến kết quả sai.
        res[i + 1] = ((res[i] - hash_char(text[i]) * BASE ** (len_pattern - 1) % MOD
                       ) * BASE + hash_char(text[i + len_pattern])) % MOD
    return res


text = input().strip()
pattern = input().strip()
hash_p = hash_pattern(pattern)
hash_t = hash_text(text, len(pattern))
res = []
for i in range(len(hash_t)):
    if hash_p == hash_t[i]:
        res.append(i)
print(res)
