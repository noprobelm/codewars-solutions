fn main() {
    let ans = nb_months(12000, 8000, 1000, 1.5);
}

fn nb_months(old: i32, new: i32, saving: i32, perc: f64) -> (i32, i32) {
    if old > new {
        return (0, old - new);
    }
    let (mut _old, mut _new, mut _saving, mut _perc): (f64, f64, f64, f64) = (old as f64, new as f64, 0.0, perc);
    let mut month: i32 = 1;
    while _old + _saving < _new {
        if month % 2 == 0 {
            _perc += 0.5;
        }
        _old = _old - _old * _perc / 100.0;
        _new = _new - _new * _perc / 100.0;
        _saving += saving as f64;
        month += 1;
    }
    let remaining = _old + _saving - _new;
    (month - 1, remaining.round() as i32)
}

#[test]
fn test_nb_months() {
    assert_eq!(nb_months(2000, 8000, 1000, 1.5), (6, 766));
    assert_eq!(nb_months(12000, 8000, 1000, 1.5), (0, 4000));
    assert_eq!(nb_months(8000, 8000, 1000, 1.5), (0, 0));
}
