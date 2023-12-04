
using System.Collections.Specialized;

var file = File.Open("../../../test.txt", FileMode.Open);
var input = new StreamReader(file).ReadToEnd().Trim().Split(Environment.NewLine);
var cards = input.Select(parseCard).ToList();

var part1 = cards
    .Where(card => card.Winners.Any())
    .Select(card => (int)Math.Pow(2, card.Winners.Count - 1))
    .Sum();

Console.WriteLine(part1);

cards.First().Cards = GetCopies(cards.First(), cards);
var part2 = cards.First().CountCards();

Console.WriteLine(part2);

static int GetCount(Card card)
{
    Console.WriteLine(card.CardNumber);
    if (card.Cards.Count == 0) return 1;
    return card.Cards.Select(GetCount).Sum();
}

static List<Card> GetCopies(Card card, List<Card> cards)
{
    var winners = card.Winners.Count;
    return cards.Skip(card.CardNumber).Take(winners).Select(x => new Card
    {
        CardNumber = x.CardNumber,
        MyNumbers = x.MyNumbers,
        WinningNumbers = x.WinningNumbers,
        Cards = GetCopies(x, cards)
    }).ToList();
}


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
    
    public List<int> Winners => WinningNumbers.Intersect(MyNumbers).ToList();

    public List<Card> Cards { get; set; } = new();

    public int CountCards()
    {
        int count = 1;

        foreach (var card in Cards)
        {
            count += card.CountCards();
        }

        return count;
    }
}
