fn main() {
    beeramid(1500, 2.0);
}

fn beeramid (bonus: i32, price: f32) -> usize {
    if bonus < 0 {
        return 0
    }
    let mut level: usize = 0;
    let mut num_beers: usize = (bonus as f32 / price) as usize;
    while level.pow(2) <= num_beers {
        num_beers -= level.pow(2);
        level += 1;
    }
    return level - 1
}

#[test]
fn test_beermaid() {
    assert_eq!(beeramid(9, 2.0), 1);
    assert_eq!(beeramid(10, 2.0), 2);
    assert_eq!(beeramid(11, 2.0), 2);
    assert_eq!(beeramid(21, 1.5), 3);
    assert_eq!(beeramid(454, 5.0), 5);
    assert_eq!(beeramid(455, 5.0), 6);
    assert_eq!(beeramid(4, 4.0), 1);
    assert_eq!(beeramid(3, 4.0), 0);
    assert_eq!(beeramid(0, 4.0), 0);
    assert_eq!(beeramid(-1, 4.0), 0);
    assert_eq!(beeramid(504, 1.7), 9);
    assert_eq!(beeramid(609, 2.2), 8);

}
