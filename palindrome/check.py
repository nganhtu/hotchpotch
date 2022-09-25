# Kiểm tra một xâu có phải là palindrome hay không.
# O(n)


def is_palindrome(string):
    i, j = 0, len(string) - 1
    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


s = input()
print(is_palindrome(s))
