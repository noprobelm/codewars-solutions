fn main() {
    find_missing(&[1, 2, 3, 4, 6, 7, 8, 9]);
}

fn find_missing(seq: &[i32]) -> i32 {
    let common_diff = (seq[seq.len() - 1] - seq[0]) / seq.len() as i32;
    if common_diff == 0 {
        return seq[0];
    }
    for (i, _) in seq.iter().enumerate().skip(1) {
        if seq[i] - seq[i - 1] != common_diff {
            return seq[i as usize - 1] + common_diff;
        }
    }
    panic!("No missing number found in the sequence");
}

#[cfg(test)]
mod tests {
    use super::find_missing;
    
    const ERR_MSG: &str = "\nYour result (left) did not match the expected output (right)";
    
    fn dotest(a: &[i32], expected: i32) {
        assert_eq!(find_missing(a), expected, "{ERR_MSG} with seq = {a:?}")
    }

    #[test]
    fn fixed_tests() {
        dotest(&[1, 2, 3, 4, 6, 7, 8, 9], 5);
        dotest(&[1, 3, 4, 5, 6, 7, 8, 9], 2);
    }
}

