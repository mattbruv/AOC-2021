use std::time::Instant;

use regex::Regex;

fn main() {
    let input = include_str!("../input.txt");
    let regex = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)").unwrap();
    let mut muls: Vec<(i32, i32, usize)> = vec![];

    for m in regex.captures_iter(input) {
        let a = m.get(1).unwrap();
        let b = m.get(2).unwrap();

        muls.push((
            a.as_str().parse().unwrap(),
            b.as_str().parse().unwrap(),
            a.start(),
        ));
    }

    let p1 = Instant::now();
    let part1: i32 = muls.iter().map(|(a, b, _)| *a * *b).sum();
    println!("Part 1: {:?} in {:?}", part1, p1.elapsed());

    let regex_do_dont = Regex::new(r"(do\(\)|don't\(\))").unwrap();

    let mut do_donts: Vec<(&str, usize)> = vec![];

    for m in regex_do_dont.captures_iter(input) {
        let cmd = m.get(1).unwrap();
        do_donts.push((cmd.as_str(), cmd.end()));
    }

    let p2 = Instant::now();
    let part2: i32 = muls
        .iter()
        .map(|(a, b, i)| {
            let latest = do_donts.iter().filter(|(_, do_i)| do_i < i).last();
            if let Some((cmd, _)) = latest {
                //println!("{}, {}, {}, {:?}", a, b, i, latest);
                if *cmd == "do()" {
                    return a * b;
                } else {
                    return 0;
                }
            }
            a * b
        })
        .sum();

    println!("Part 2: {:?} in {:?}", part2, p2.elapsed());
}
