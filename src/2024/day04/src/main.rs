type Pos = (isize, isize);
type Word = [Pos; 4];

fn main() {
    let input = include_str!("../test.txt");
    let word_search: Vec<Vec<char>> = input.lines().map(|l| l.chars().collect()).collect();

    for (y, row) in word_search.iter().enumerate() {
        for (x, _) in row.iter().enumerate() {
            let words =
                check_words_at(&word_search, (x.try_into().unwrap(), y.try_into().unwrap()));
            println!("{}, {}: {:?}", x, y, words);
            // look up each position, add results to hash map
            // make sure to sort words by positions for hash map
        }
    }

    /*
        println!("{:?}", word_search);
        println!(
            "test: {:?}",
            get_word_at(&word_search, (0, 0), &[(0, 0), (1, 1), (2, 2), (3, 3)])
        );
    */
}

fn reverse(s: &String) -> String {
    s.chars().rev().collect()
}

fn check_words_at(word_search: &Vec<Vec<char>>, position: Pos) -> Vec<Vec<Pos>> {
    let offsets: Vec<Word> = vec![
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (1, 1), (2, 2), (3, 3)],
        [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
    ];

    let words: Vec<(String, Vec<Pos>)> = offsets
        .iter()
        .map(|w| get_word_at(word_search, position, w))
        .filter(|x| x.0.eq("XMAS") || reverse(&x.0).eq("SAMX"))
        .collect();

    words.iter().map(|x| x.1.clone()).collect()
}

fn get_word_at(word_search: &Vec<Vec<char>>, (x, y): Pos, direction: &Word) -> (String, Vec<Pos>) {
    let mut word = String::new();
    let mut positions: Vec<Pos> = vec![];

    direction.iter().for_each(|(dx, dy)| {
        //println!("{}, {}", y, dy);
        let oy: Result<usize, _> = (y + dy).try_into();
        if let Ok(offset_y) = oy {
            let a = word_search.iter().nth(offset_y);
            if let Some(chars) = a {
                let ox: Result<usize, _> = (x + dx).try_into();
                if let Ok(offset_x) = ox {
                    let b = chars.iter().nth(offset_x);
                    if let Some(magical_character) = b {
                        word.push(*magical_character);
                        positions.push((offset_x as isize, offset_y as isize));
                    }
                }
            }
        }
    });

    (word, positions)
}
