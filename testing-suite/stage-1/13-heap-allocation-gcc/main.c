#include <stdio.h>
#include <stdlib.h>

#define ARRAY_SIZE 3

int* get_values();

int main() {
    int* values = get_values();

    for (int i = 0; i < ARRAY_SIZE; i++) {
        printf("value: %d\n", values[i]);
    }

    free(values);

    return 0;
}

int* get_values() {
    int* to_return = malloc(sizeof(int) * ARRAY_SIZE);
    to_return[0] = 1;
    to_return[1] = 2;
    to_return[2] = 3;

    return to_return;
}
