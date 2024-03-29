// `NanoSecond` is a new name for `u64`
type NanoSecond = u64;
type Inch = u64;

#[allow(non_camel_case_types)]
// Use an attribute to silence warning
type u64_t = u64;
// TODO ^ try removing the attribute

fn main() {
    // `NanoSecond` = `Inch` = `u64_t` = `u64`.
    let nanoseconds: NanoSecond = 5 as u64_t;
    let inches: Inch = 2 as u64_t;

    // Note that type aliases *don't* provide any extra type safety, because
    // aliases are *not* new types
    println!("{} nanoseconds + {} inches = {} unit?",
             nanoseconds,
             inches,
             nanoseconds + inches);
}
