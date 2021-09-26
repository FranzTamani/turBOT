#include <iostream>
#include <memory>

struct Foo {
    int a;
    int b;
};

std::unique_ptr<Foo> get_values();

int main() {
    auto values = get_values();
    std::cout << "a: " << values->a << "\n";
    std::cout << "b: " << values->b << std::endl;

    return 0;
}

std::unique_ptr<Foo> get_values() {
    return std::make_unique<Foo>(Foo{1, 2});
}
