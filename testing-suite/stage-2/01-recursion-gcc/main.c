#include <stdio.h>

int to_1000(int x) {
    x++;
    if (x >= 1000) return x;
    else return to_1000(x);
}

int main() {
    int i = to_1000(0);
    printf("done: %d\n", i);

    return 0;
}
