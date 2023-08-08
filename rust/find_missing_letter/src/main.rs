fn main() {
    let chars = ['a', 'b', 'c', 'd', 'f'];
    let missing = find_missing_letter(&chars).expect("No missing letter was found");
    println!("{missing}");
}

fn find_missing_letter(chars: &[char]) -> Option<char> {
    let unicode: Vec<u32> = chars.iter().map(|&c| c as u32).collect();
    let first: u32 = unicode[0];
    let last: u32 = *unicode.last().expect("Vector is empty");

    let complete: Vec<u32> = (first..last + 1).collect();

    for i in complete {
        if !unicode.contains(&i) {
            return Some(
                char::from_u32(i).expect("Expected u32 for unicode representation of char"),
            );
        }
    }

    None
}
