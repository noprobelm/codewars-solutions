fn main() {
    split_and_add(&[1,2,3,4,5], 2);
}

fn split_and_add(arr: &[u32], n: usize) -> Vec<u32> {
    let mut arr = arr.to_vec();
    for _ in 0..n {
        let first = arr.drain(0..arr.len() / 2).collect::<Vec<_>>();
        let second = arr.drain(0..arr.len()).collect::<Vec<_>>();
        arr = first.iter().rev().zip(second.iter().rev()).map(|(a, b)| a + b).collect();
        if first.len() != second.len() {
            arr.push(second[0])
        }
        arr.reverse();
    }
    arr
}

#[test]
    fn test_split_and_add() {
        assert_eq!(split_and_add(&[1,2,3,4,5], 2), vec![5,10]);
        assert_eq!(split_and_add(&[1,2,3,4,5], 3), vec![15]);
        assert_eq!(split_and_add(&[15], 3), vec![15]);
        assert_eq!(split_and_add(&[32,45,43,23,54,23,54,34], 2), vec![183, 125]);
        assert_eq!(split_and_add(&[32,45,43,23,54,23,54,34], 0), vec![32,45,43,23,54,23,54,34]);
        assert_eq!(split_and_add(&[3,234,25,345,45,34,234,235,345], 3), vec![305, 1195]);
        assert_eq!(split_and_add(&[3,234,25,345,45,34,234,235,345,34,534,45,645,645,645,4656,45,3], 4), vec![1040, 7712]);
        assert_eq!(split_and_add(&[23,345,345,345,34536,567,568,6,34536,54,7546,456], 20), vec![79327]);
    }


