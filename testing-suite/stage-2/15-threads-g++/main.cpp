#include <iostream>
#include <thread>
#include <chrono>

void* thread_fun() {
    std::cout << "we threading" << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(1));
    std::cout << "we still threading" << std::endl;

    return NULL;
}

int main() {
    pthread_t thread_id;
    std::cout << "starting the thread" << std::endl;
    std::thread t(thread_fun);
    t.join();
    std::cout << "the thread has finished" << std::endl;

    return 0;
}
