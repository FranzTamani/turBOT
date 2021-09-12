#ifndef FOO_H
#define FOO_H

class Foo {
public:
    Foo(int _a, int _b);
    int get_a();
    int get_b();
    static int get_c();
    static void set_c(int val);

private:
    int a;
    int b;
    inline static int c;
};

Foo::Foo(int _a, int _b) {
    a = _a;
    b = _b;
}

int Foo::get_a() {
    return a;
}

int Foo::get_b() {
    return b;
}

int Foo::get_c() {
    return c;
}

void Foo::set_c(int val) {
    c = val;
}

#endif
