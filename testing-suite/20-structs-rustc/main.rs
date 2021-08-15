fn main() {
    let f = Foo::new(1, 2);

    println!("a: {}", f.get_a());
    println!("b: {}", f.get_b());

    return
}

struct Foo {
    a: i32,
    b: i32,
}

impl Foo {
    fn new(a: i32, b: i32) -> Foo {
        Foo {
            a,
            b,
        }
    }

    fn get_a(&self) -> i32 {
        self.a
    }

    fn get_b(&self) -> i32 {
        self.b
    }
}
