fn main() {
    amount_of_pages(25);
}

fn amount_of_pages(summary: u32) -> u32 {
    let mut num_pages: u32 = 0;
    let digits: Vec<u32> = (1..=summary).map(|x| format!("{x}").len() as u32).collect();
    for (i, d) in digits.iter().enumerate() {
        num_pages += d;
        if num_pages == summary {
            return (i + 1) as u32;
        }
    }
    panic!("No answer found for summary '{summary}'!")
}

#[test]
fn test_amount_of_pages() {
    assert_eq!(amount_of_pages(5), 5);
    assert_eq!(amount_of_pages(25), 17);
    assert_eq!(amount_of_pages(1095), 401);
    assert_eq!(amount_of_pages(185), 97);
    assert_eq!(amount_of_pages(660), 256);
}
