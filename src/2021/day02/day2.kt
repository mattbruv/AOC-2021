// kotlinc day2.kt -include-runtime -d day2.jar

import java.io.File;

fun main() {
    println("Hello, world!")
    val input = File("input.txt").useLines { it.toList() }
    val instrs = input.map { parse(it) }
    println(part1(instrs))
    println(part2(instrs))
}

fun part1(instrs: List<Pair<String, Int>>): Int {
    var depth = 0;
    var horiz = 0;
    instrs.forEach {
        when (it.first) {
            "forward" -> horiz += it.second
            "down" -> depth += it.second
            "up" -> depth -= it.second
            else -> {}
        }
    }
    return depth * horiz;
}

fun part2(instrs: List<Pair<String, Int>>): Int {
    var depth = 0;
    var horiz = 0;
    var aim = 0;
    instrs.forEach {
        when (it.first) {
            "forward" -> { 
                horiz += it.second
                depth += (aim * it.second)
            }
            "down" -> aim += it.second
            "up" -> aim -= it.second
            else -> {}
        }
    }
    return depth * horiz;
}

fun parse(line: String): Pair<String, Int> {
    val info = line.split(" ")
    return Pair(info[0], info[1].toInt())
}