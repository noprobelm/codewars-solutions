fn main() {
    let answer = high_and_low("1 2 3 4 5");
    println!("{answer}");
}

fn high_and_low(numbers: &str) -> String {
    let parsed: Vec<i32> = numbers
        .split_whitespace()
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();

    match (parsed.iter().min(), parsed.iter().max()) {
        (Some(min), Some(max)) => format!("{} {}", max, min),
        _ => String::from("No min and max values found in vector"),
    }
}
