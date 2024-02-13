fn josephus_survivor(n: i32, k: i32) -> i32 {
    let mut players: Vec<i32> = (1..=n).collect();
    let mut i = 0;
    while players.len() > 1 {
        i = (i + k as usize - 1) % players.len();
        players.remove(i);
    }
    players[0]
}

#[test]
fn test_josephus_survivor() {
    assert_eq!(josephus_survivor(7, 3), 4)

}
