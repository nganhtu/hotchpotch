#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

int countDigit(int n) {
    if (n == 0) {
        return 1;
    }
    return ceil(log10((double)n + 0.5));
}

int getFirstDigit(int n) {
    if (n == 0) {
        return 0;
    }
    return n / (int)pow(10, countDigit(n) - 1);
}

bool compAsc(int a, int b) {
    if (getFirstDigit(a) != getFirstDigit(b)) {
        return getFirstDigit(a) < getFirstDigit(b);
    }

    // Handle the case when 2nd leading digit is 0
    int countDigitA = countDigit(a), countDigitB = countDigit(b),
        _a = a - getFirstDigit(a) * (int)pow(10, countDigitA - 1),
        _b = b - getFirstDigit(b) * (int)pow(10, countDigitB - 1);
    if (countDigitA - countDigit(_a) == countDigitB - countDigit(_b)) {
        return compAsc(_a, _b);
    }
    if (a % 10 != 0 && b % 10 != 0) {
        return countDigitA - countDigit(_a) > countDigitB - countDigit(_b);
    }
    if (a % 10 == 0 && b % 10 == 0) {
        return countDigitA - countDigit(_a) < countDigitB - countDigit(_b);
    }
    if (a % 10 == 0) {
        return true;
    }
    if (b % 10 == 0) {
        return false;
    }

    cout << endl
         << "ERROR in compAsc() function~" << endl;
    return true;
}

int main() {
    vector<int> arr = {1, 3, 5, 100, 101, 10, 12, 1000, 23};

    sort(arr.begin(), arr.end(), compAsc);

    for (int num : arr) {
        cout << (num) << " ";
    }

    return 0;
}
