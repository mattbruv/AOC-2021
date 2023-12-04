// See https://aka.ms/new-console-template for more information



var file = File.Open("../../../input.txt", FileMode.Open);
var input = new StreamReader(file).ReadToEnd().Trim().Split(Environment.NewLine);
var cards = input.Select(parseCard).ToList();

var part1 = cards
    .Select(card => card.MyNumbers.Where(n => card.WinningNumbers.Contains(n)).ToList())
    .Select(ns => (int)(Math.Pow(2, ns.Count - 1)))
    .Sum();

Console.WriteLine(part1);

static List<int> toInts(List<string> strings)
{
    return strings.Select(str => int.TryParse(str, out int number) ? number : (int?)null)
        .Where(num => num.HasValue)
        .Select(num => num.Value).ToList();
}

static Card parseCard(string line)
{
    var data = line.Split(":");
    var numbers = data[1].Split("|");
    var id =  Int32.Parse(data[0].Substring(4));

    return new Card
    {
          CardNumber = id,
          WinningNumbers = toInts(numbers[0].Split(" ").ToList()),
          MyNumbers = toInts(numbers[1].Split(" ").ToList()),
    };
} 

class Card
{
    public int CardNumber { get; set; }
    public List<int> WinningNumbers { get; set; } = new();
    public List<int> MyNumbers { get; set; } = new();
}