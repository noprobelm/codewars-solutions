fn main() {
    let ans = josephus_survivor(7, 3);
    println!("The survivor with 7 players and k=3 is: {}", ans);
}

fn josephus_survivor(n: i32, k: i32) -> i32 {
    let mut players: Vec<i32> = (1..=n).collect();
    let mut i = 0;
    while players.len() > 1 {
        i = (i + k as usize - 1) % players.len();
        println!("i: {}", i);
        players.remove(i);
    }
    players[0]
}

#[test]
fn test_josephus_survivor() {
    assert_eq!(josephus_survivor(7, 3), 4);
    assert_eq!(josephus_survivor(11, 19), 10);
    assert_eq!(josephus_survivor(40, 3), 28);
    assert_eq!(josephus_survivor(14, 2), 13);
    assert_eq!(josephus_survivor(100, 1), 100);
    assert_eq!(josephus_survivor(1, 300), 1);
    assert_eq!(josephus_survivor(2, 300), 1);
    assert_eq!(josephus_survivor(5, 300), 1);
    assert_eq!(josephus_survivor(7, 300), 7);
    assert_eq!(josephus_survivor(300, 300), 265);
}
