fn main() {
    println!("255,255,255 is {} in hexadecimal", rgb(255, 255, 255));
}

fn rgb(r: i32, g: i32, b: i32) -> String {
    let mut nums: Vec<i32> = Vec::new();
    for n in [r, g, b] {
        if n < 0 {
            nums.push(0)
        }
        else if n > 255 {
            nums.push(255)
        }
        else {
            nums.push(n)
        }
    }
    nums.iter().map(|x| format!("{:0>2X}", x)).collect::<Vec<String>>().join("")
}

#[test]
fn test_rgb() {
    assert_eq!(rgb(255, 255, 255), "FFFFFF");
    assert_eq!(rgb(255, 255, 300), "FFFFFF");
    assert_eq!(rgb(0, 0, 0), "000000");
    assert_eq!(rgb(148, 0, 211), "9400D3");
}
