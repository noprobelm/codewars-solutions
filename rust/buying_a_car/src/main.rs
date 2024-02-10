fn nb_months(old: i32, new: i32, saving: i32, perc: f64) -> (i32, i32) {
    if old > new {
        return (0, old - new);
    }
    let (mut old, mut new, mut savings_accrued, mut perc): (f64, f64, f64, f64) = (old as f64, new as f64, 0.0, 1_f64 - (perc / 100_f64));

    let mut month: i32 = 0;

    while old + savings_accrued < new {
        month += 1;

        if month % 2 == 0 {
            perc -= 0.005
        }

        old *= perc;
        new *= perc;
        savings_accrued += saving as f64;
    }

    let remaining = old + savings_accrued - new;
    (month, remaining.round() as i32)
}

#[test]
fn test_nb_months() {
    assert_eq!(nb_months(2000, 8000, 1000, 1.5), (6, 766));
    assert_eq!(nb_months(12000, 8000, 1000, 1.5), (0, 4000));
    assert_eq!(nb_months(8000, 8000, 1000, 1.5), (0, 0));
}
