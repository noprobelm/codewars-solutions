fn main() {
    let word: &str = "test";
    get_middle(word);
}

fn get_middle(s: &str) -> &str {
    let end: usize = s.len() / 2;
    let mut start: usize = end;
    if s.len() % 2 == 0 {
        start = end - 1;
    }
    let middle = &s[start..end + 1];
    &middle
}
