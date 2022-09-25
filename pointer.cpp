#include <bits/stdc++.h>

using namespace std;

int main() {
    int a = 1234;
    int *p = &a;
    printf("%d %d %d\n", p, *p, &p);

    return 0;
}
