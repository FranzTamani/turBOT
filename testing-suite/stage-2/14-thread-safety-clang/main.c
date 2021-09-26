#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

int resource = 0;
int running = 1;
pthread_mutex_t lock;

void* producer() {
    while (running) {
        pthread_mutex_lock(&lock);
        if (resource == 0) {
            resource = rand() % 100 + 1;
        } else {
            printf("resource not consumed, cannot produce\n");
        }
        pthread_mutex_unlock(&lock);
        sleep(1);
    }

    return NULL;
}

void* consumer() {
    while (running) {
        pthread_mutex_lock(&lock);
        if (resource != 0) {
            printf("consumed resource: %d\n", resource);
            resource = 0;
        } else {
            printf("resource not produced, cannot consume\n");
        }
        pthread_mutex_unlock(&lock);
        sleep(1);
    }

    return NULL;
}

int main() {
    pthread_mutex_init(&lock, NULL);
    srand(2049); // this is your fault jackson

    pthread_t producer_thread, consumer_thread;
    pthread_create(&producer_thread, NULL, producer, NULL);
    pthread_create(&consumer_thread, NULL, consumer, NULL);

    sleep(5);
    running = 0;

    pthread_join(producer_thread, NULL);
    pthread_join(consumer_thread, NULL);
    pthread_mutex_destroy(&lock);

    return 0;
}
