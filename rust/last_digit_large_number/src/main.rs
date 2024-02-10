fn main() {
    let answer: i32 = last_digit("1606938044258990275541962092341162602522202993782792835301373","2037035976334486086268445688409378161051468393665936250636140449354381299763336706183397376");
}

fn last_digit(str1: &str, str2: &str) -> i32 {
    let mut pattern: Vec<u32> = vec![];
    let s1_last: u32 = str1.chars().last().unwrap().to_digit(10).unwrap();

    let answer = match s1_last {
        answer < 2 => s1_last;
        _ =>

    }

    pattern.push(s1_last);
    let mut product_last: u32 = (s1_last * s1_last)
        .to_string()
        .chars()
        .last()
        .unwrap()
        .to_digit(10)
        .unwrap();


    while product_last != s1_last {
        product_last = (product_last * s1_last)
            .to_string()
            .chars()
            .last()
            .unwrap()
            .to_digit(10)
            .unwrap();
        pattern.push(product_last);
    }

    println!("{:?}", pattern);

    let answer: i32 = 5;
    answer
}
