#include <stdio.h>

int main() {
    FILE* f = fopen("test.txt", "w");;
    if (f == NULL) {
        printf("failed to open for writing\n");
        return 1;
    }

    fprintf(f, "can i get uhhhhh boneless pizza wit a 2 litre coke");
    fclose(f);

    f = fopen("test.txt", "r");
    if (f == NULL) {
        printf("failed to open for reading\n");
        return 1;
    }

    char str[256];
    fgets(str, sizeof(char) * 256, f);
    printf("read: %s\n", str);
    fclose(f);

    return 0;
}
