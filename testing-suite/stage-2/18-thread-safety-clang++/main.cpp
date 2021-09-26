#include <iostream>
#include <thread>
#include <chrono>
#include <mutex>
#include <stdlib.h>

int resource = 0;
bool running = true;
std::mutex lock;

void* producer() {
    while (running) {
        lock.lock();
        if (resource == 0) {
            resource = rand() % 100 + 1;
        } else {
            std::cout << "resource not consumed, cannot produce" << std::endl;
        }
        lock.unlock();
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    return NULL;
}

void* consumer() {
    while (running) {
        lock.lock();
        if (resource != 0) {
            std::cout << "consumed resource: " << resource << std::endl;
            resource = 0;
        } else {
            std::cout << "resource not produced, cannot consume" << std::endl;
        }
        lock.unlock();
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    return NULL;
}

int main() {
    srand(2049); // this is your fault jackson

    std::thread p(producer);
    std::thread c(consumer);

    std::this_thread::sleep_for(std::chrono::seconds(5));
    running = false;

    p.join();
    c.join();

    return 0;
}
