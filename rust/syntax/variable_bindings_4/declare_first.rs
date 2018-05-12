fn main() {
    // Declare a variable binding
    let a_binding;

    {
        let x = 2;

        // Initialize the binding
        a_binding = x * x;
    }

    println!("a binding: {}", a_binding);

    let another_binding;

    // Error! Use of uninitialized binding
    //println!("another biding: {};", another_binding);
    // FIXME ^ Comment ou this line

    another_binding = 1;

    println!("another binding: {}", another_binding);
}
