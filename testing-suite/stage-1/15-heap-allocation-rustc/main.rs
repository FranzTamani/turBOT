fn main() {
    let values = get_values();
    for v in 0..values.len() {
        println!("value: {}", v);
    }

    return
}

fn get_values() -> Box<[i32; 3]> {
    Box::new([1, 2, 3])
}
