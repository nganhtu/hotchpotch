#include <bits/stdc++.h>

using namespace std;

void checkEndian() {
    int x = 1;  // 0x00000001
    if (*(char *)&x) {
        /* little endian. memory image 01 00 00 00 */
        cout << "little";
    } else {
        /* big endian. memory image 00 00 00 01 */
        cout << "big";
    }
}

int main() {
    checkEndian();

    return 0;
}
