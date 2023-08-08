fn main() {
    let xs: [u32; 7] = [1, 1, 1, 1, 1, 1, 2];
    let num: u32 = stray(&xs);
    println!("{num}");
}

fn stray(arr: &[u32]) -> u32 {
    let stray: u32;

    let mut vec = arr.to_vec();
    vec.sort();

    let first = vec.first().expect("Array is empty");

    if vec.iter().filter(|&x| x == first).count() == 1 {
        stray = *first
    } else {
        stray = *vec.last().expect("Array is empty")
    }

    stray
}
