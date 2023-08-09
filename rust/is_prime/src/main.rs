fn main() {
    let num: i64 = 2;
    let answer: bool = is_prime(num);
    println!("{answer}")
}

fn is_prime(x: i64) -> bool {
    if x <= 1 {
        return false;
    } else if x == 2 {
        return true;
    }

    let sqrt = f64::sqrt(x as f64) as i64 + 1;
    for n in (2..sqrt + 1) {
        if x % n == 0 {
            return false;
        }
    }

    true
}
