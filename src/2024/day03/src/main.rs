use regex::Regex;

fn main() {
    let input = include_str!("../input.txt");
    let regex = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)").unwrap();
    let mut muls: Vec<(i32, i32)> = vec![];

    for (_, [a, b]) in regex.captures_iter(input).map(|c| c.extract()) {
        muls.push((a.parse().unwrap(), b.parse().unwrap()));
    }

    let part1: i32 = muls.iter().map(|(a, b)| *a * *b).sum();
    println!("{:?}", part1);
}
