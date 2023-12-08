use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

#[derive(Debug)]
struct Map {
    seeds: Vec<u64>,
    seed_to_soil: Vec<Vec<u64>>,
    soil_to_fertilizer: Vec<Vec<u64>>,
    fertilizer_to_water: Vec<Vec<u64>>,
    water_to_light: Vec<Vec<u64>>,
    light_to_temperature: Vec<Vec<u64>>,
    temperature_to_humidity: Vec<Vec<u64>>,
    humidity_to_location: Vec<Vec<u64>>,
}

fn main() -> io::Result<()> {
    let path = Path::new("input.txt");
    let file = File::open(&path)?;
    let reader = io::BufReader::new(file);

    let mut map = Map {
        seeds: vec![],
        seed_to_soil: vec![],
        soil_to_fertilizer: vec![],
        fertilizer_to_water: vec![],
        water_to_light: vec![],
        light_to_temperature: vec![],
        temperature_to_humidity: vec![],
        humidity_to_location: vec![],
    };

    let mut current_map = 0;

    for line in reader.lines() {
        let line = line?;
        if line.is_empty() {
            current_map += 1;
            continue;
        }

        let numbers: Vec<u64> = line
            .split_whitespace()
            .filter_map(|s| s.parse().ok())
            .collect();

        match current_map {
            0 => map.seeds = numbers,
            1 => map.seed_to_soil.push(numbers),
            2 => map.soil_to_fertilizer.push(numbers),
            3 => map.fertilizer_to_water.push(numbers),
            4 => map.water_to_light.push(numbers),
            5 => map.light_to_temperature.push(numbers),
            6 => map.temperature_to_humidity.push(numbers),
            7 => map.humidity_to_location.push(numbers),
            _ => (),
        }
    }

    println!("{:#?}", map);

    Ok(())
}
