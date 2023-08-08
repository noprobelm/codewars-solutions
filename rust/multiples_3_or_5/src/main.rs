fn main() {
    let num: i32 = 33;
    let answer = solution(num);

fn solution(num: i32) -> i32 {
    (0..num).filter(|&i| i % 3 == 0 || i % 5 == 0).sum()
}
