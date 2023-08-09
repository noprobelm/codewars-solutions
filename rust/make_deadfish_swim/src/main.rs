fn main() {
    println!("Hello, world!");
    parse("iiisdoso");
}

fn parse(code: &str) -> Vec<i32> {
    let mut num: i32 = 0;
    let mut output: Vec<i32> = vec![];
    for i in code.chars() {
        match i {
            'i' => num += 1,
            'd' => num -= 1,
            's' => num *= num,
            'o' => output.push(num),
            _ => println!("Invalid code"),
        }
    }
    output
}
