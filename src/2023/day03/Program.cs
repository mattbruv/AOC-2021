using System.Formats.Tar;
using System.Text.RegularExpressions;

var lines = File.ReadAllLines("../../../test.txt");
var characterGrid = lines.Select(x => x.ToList()).ToList();

var numbers = lines
    .SelectMany(ParseNumbers)
    .Select(n => new
    {
        Number = n,
        surroundingChars = n.Indicies
            .SelectMany(i => GetSurroundingCharacters(i.X, i.Y, characterGrid))
            .Where(c => char.IsNumber(c.Value) == false && c.Value != '.')
            .DistinctBy(z => (z.X, z.Y))
    })
    .ToList();
// select numbers with their row


Console.WriteLine(numbers);

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
        .Where(offset => offset.X >= 0 && offset.X <= xMax)
        .Where(offset => offset.Y >= 0 && offset.Y <= yMax)
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
    public List<(int X, int Y)> Indicies => Enumerable.Range(Index, Index + Value.Length).Select(x => (x, Row)).ToList();
    public string Value { get; set; }
    public int AsNumber => Int32.Parse(Value);
}