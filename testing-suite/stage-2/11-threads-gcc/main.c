#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

void* thread_fun() {
    printf("we threading\n");
    sleep(1);
    printf("we still threading\n");

    return NULL;
}

int main() {
    pthread_t thread_id;
    printf("starting the thread\n");
    pthread_create(&thread_id, NULL, thread_fun, NULL);
    pthread_join(thread_id, NULL);
    printf("the thread has finished\n");

    return 0;
}
