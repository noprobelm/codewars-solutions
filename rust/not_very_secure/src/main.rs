fn alphanumeric(password: &str) -> bool {
    password.len() != 0usize && password.chars().all(|c| c.is_alphanumeric())
}

#[test]
fn test_alphanumeric() {
    assert_eq!(alphanumeric("hello world_"), false);
    assert_eq!(alphanumeric("PassW0rd"), true);
    assert_eq!(alphanumeric("     "), false);
}
