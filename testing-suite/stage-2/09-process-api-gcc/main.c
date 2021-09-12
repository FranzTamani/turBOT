#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int res = fork();
    if (res < 0) { // process creation failed
        printf("failed to fork\n");
        return 1;
    } else if (res == 0) { // child process
        int i = 0;
        do {
            printf("we are legion\n");
            i++;
        } while (i < 5);
    } else { // parent process
        wait(NULL);
        printf("aight im out\n");
    }

    return 0;
}
