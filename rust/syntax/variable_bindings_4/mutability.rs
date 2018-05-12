fn main() {
    let _immutable_binding = 1;
    let mut mutable_binding = 1;

    println!("Before mutation: {}", mutable_binding);

    // OK
    mutable_binding += 1;

    println!("After mutation: {}", mutable_binding);

    // Error!
    //_immutable_binding += 1;
    // FIXME ^ Comment out this line
}
