#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* concat(const char* a, const char* b) {
    char* to_return = malloc(sizeof(char) * 256);
    strcpy(to_return, a);
    strcat(to_return, b);

    return to_return;
}

int main() {
    char* res = concat("yeah", "nah");
    printf("%s\n", res);
    free(res);

    return 0;
}
