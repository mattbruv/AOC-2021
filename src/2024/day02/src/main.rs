use std::time::Instant;

fn main() {
    let input = include_str!("../input.txt");

    let reports: Vec<Vec<i32>> = input
        .lines()
        .map(|x| x.split_whitespace().map(|x| x.parse().unwrap()).collect())
        .collect();

    let p1 = Instant::now();
    let part1: Vec<&Vec<i32>> = reports
        .iter()
        .filter(|report: &&Vec<i32>| is_report_safe(*report))
        .collect();
    //.count();

    println!("Part 1: {:?} in {:?}", part1.iter().count(), p1.elapsed());

    let p2 = Instant::now();
    let part2: Vec<&Vec<i32>> = reports
        .iter()
        .filter(|report| is_report_safe(report) || try_different_lists(report))
        .collect();

    println!("Part 2: {:?} in {:?}", part2.iter().count(), p2.elapsed());
}

fn is_report_safe(report: &Vec<i32>) -> bool {
    let mut decreasing = false;
    let mut increasing = false;
    let test = report.iter().enumerate().all(|(index, n)| {
        let current = n;
        let maybe_next = report.get(index + 1);

        if let Some(next) = maybe_next {
            let diff = current - next;
            if diff < 0 {
                decreasing = true;
            } else if diff > 0 {
                increasing = true;
            } else {
                return false;
            }
            if diff.abs() > 3 {
                return false;
            }
        }

        return increasing != decreasing;
    });

    test
}

fn try_different_lists(report: &Vec<i32>) -> bool {
    for (i, _) in report.iter().enumerate() {
        let new_report: Vec<i32> = report
            .iter() //
            .enumerate()
            .filter(|e| e.0 != i)
            .map(|x| *x.1)
            .collect();

        if is_report_safe(&new_report) {
            return true;
        }
    }

    false
}
