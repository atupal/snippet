pub fn public_function() {
    println!("called rary's `public_functin()`");
}

fn private_function() {
    println!("called rary's `private_function`");
}

pub fn indirect_access() {
    println!("called rary's `indirect_access()`, that\n>");

    private_function();
}
