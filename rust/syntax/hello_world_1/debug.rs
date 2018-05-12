// This structure cannot be printed either with `fmt::Display` or
// with `fmt::Debug`
struct UnPrintable(i32);

// The `derive` attribute automatically creates the implementation
// required to make this `struct` ptintable with `fmt::Debug`.
#[derive(Debug)]
struct DebugPrintable(i32);


// Deriveructure the `fmt::Debug` implementation for `Structure`. `Structure`
// is a structure which contains a single `i32`
#[derive(Debug)]
struct Structure(i32);

// Put a `Strcture` inside of the structure `Deep`. Make it printable
// also.
#[derive(Debug)]
struct Deep(Structure);

fn main() {
    // Printing with `{:?}` is similar to with `{}`.
    println!("{:?} months is a year", 12);
    println!("{1:?} {0:?} is the {actor:?} name.",
             "Slater",
             "Christian",
             actor = "actor's");

    // `Structure` is printable!
    println!("Now {:?} will print!", Structure(3));

    // The problem with `derive` is there is no control over how
    // the results look. What if I want this to just whow a `7`?
    println!("Now {:?} will print!", Deep(Structure(7)));
}
