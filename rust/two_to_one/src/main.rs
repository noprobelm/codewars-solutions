fn main() {
    let answer = longest("xyaabbbccccdefww", "xxxxyyyyabklmopq");
    println!("{answer}");
}

fn longest(a1: &str, a2: &str) -> String {
    let mut chars: Vec<char> = format!("{}{}", a1, a2).chars().collect();
    chars.sort();
    chars.dedup();
    chars.iter().collect::<String>()
}
