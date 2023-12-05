// I hope I never have to look at this godforsaken file again
// spent like 3 hours on this bullshit

using System.Text.RegularExpressions;

var lines = File.ReadAllLines("../../../input.txt");
var characterGrid = lines.Select(x => x.ToList()).ToList();

var numbers = lines
    .SelectMany(ParseNumbers)
    .Select(n => new
    {
        Number = n,
        surroundingChars = n.Indicies
            .SelectMany(i => GetSurroundingCharacters(i.X, i.Y, characterGrid))
            .Where(c => char.IsNumber(c.Value) == false && c.Value != '.')
            .DistinctBy(z => (z.X, z.Y)).ToList()
    })
    .ToList();


var part1 = numbers
    .Where(n => n.surroundingChars.Any())
    .Sum(n => n.Number.AsNumber);

// // LINQ query to count unique ints for each Test instance
// var result = tupleList.GroupBy(t => t.Item2)
  //  .Select(group => new { TestInstance = group.Key, UniqueIntCount = group.Select(t => t.Item1).Distinct().Count() });

var part2 = numbers
    .Where(n => n.surroundingChars.Count == 1 && n.surroundingChars.First().Value == '*')
    .Select(x => new { x.Number, Char = (x.surroundingChars.First().X, x.surroundingChars.First().Y) })
    .GroupBy(x => $"{x.Char.X}-{x.Char.Y}")
    .Select(x => new {Coord = x.Key, Value = x.ToList() })
    .Where(x => x.Value.Count == 2)
    .Select(x => x.Value[0].Number.AsNumber * x.Value[1].Number.AsNumber)
    .Sum();


Console.WriteLine(part1);
Console.WriteLine(part2);

return;

// A list of numbers and their X, Y coordinates
// A function that takes a character X, Y and returns the surrounding characters in a list

static List<ParsedCharacter> GetSurroundingCharacters(int x, int y, List<List<char>> grid)
{
    List<(int X, int Y)> offsets = new()
    {
        (x - 1, y - 1),
        (x - 0, y - 1),
        (x + 1, y - 1),
        (x - 1, y - 0),
        // (x - 0, y - 0),
        (x + 1, y - 0),
        (x - 1, y + 1),
        (x + 0, y + 1),
        (x + 1, y + 1),
    };

    var xMax = grid.First().Count;
    var yMax = grid.Count;

    return offsets
        .Where(offset => offset.X >= 0 && offset.X < xMax)
        .Where(offset => offset.Y >= 0 && offset.Y < yMax)
        .Select(offset => new ParsedCharacter
        {
            Value = grid[offset.Y][offset.X],
            X = offset.X,
            Y = offset.Y
        })
        .ToList();
}

static List<ParsedNumber> ParseNumbers(string line, int row)
{
    var pattern = @"\d+";
    var rg = new Regex(pattern);
    var matches = rg.Matches(line);
    return matches.Select(match => new ParsedNumber
    {
        Value = match.Value,
        Index = match.Index,
        Row = row
    }).ToList();
}

class ParsedCharacter
{
    public int X { get; set; }
    public int Y { get; set; }
    public char Value { get; set; }
}
class ParsedNumber
{
    public int Index { get; set; }
    public int Row { get; set; }
    public List<(int X, int Y)> Indicies => Enumerable.Range(Index, Value.Length).Select(x => (x, Row)).ToList();
    public string Value { get; set; }
    public int AsNumber => Int32.Parse(Value);
}