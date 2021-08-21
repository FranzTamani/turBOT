#include <iostream>

#include "foo.h"

int main() {
    Foo* f = new Foo(1, 2);
    Foo::set_c(3);

    std::cout << "a: " << f->get_a() << "\n";
    std::cout << "b: " << f->get_b() << "\n";
    std::cout << "c: " << Foo::get_c() << std::endl;

    delete f;

    return 0;
}
