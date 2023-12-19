use std::fs::File;
use std::io::{self, BufRead, Read};
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

fn main() {
    let path = Path::new("input.txt");
    let file = std::fs::read_to_string(path).unwrap();
    let parts: Vec<&str> = file.split("\n\n").collect();

    println!("{:?}", parts)
}
