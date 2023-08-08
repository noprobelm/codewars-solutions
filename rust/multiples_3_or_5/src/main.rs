fn main() {
    let num: i32 = 33;
    let answer = solution(num);
    println!("{answer}")
}

fn solution(num: i32) -> i32 {
    let range: Vec<i32> = (0..num).collect();
    let mut multiples: Vec<i32> = vec![];

    if range.is_empty() {
        return 0;
    }

    for i in range {
        if i % 3 == 0 || i % 5 == 0 {
            multiples.push(i);
        }
    }

    return multiples.iter().fold(0, |acc, el| acc + el);
}
