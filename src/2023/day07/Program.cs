
Console.WriteLine("Hello, World!");

var input = File.ReadAllLines("../../../input.txt");
var hands = input.Select(parseHand).ToList();


var ordered = hands
    .OrderBy(x => x.FiveOfAKind)
    .ThenBy(x => x.FourOfAKind)
    .ThenBy(x => x.FullHouse)
    .ThenBy(x => x.ThreeOfAKind)
    .ThenBy(x => x.TwoPair)
    .ThenBy(x => x.OnePair)
    .ThenBy(x => x.HighCard)
    .ThenBy(x => x.Score)
    .ToList();

var part1 = ordered
    .Select((Hand, Index) => new { Hand, Index })
    .Select(x => x.Hand.Bid * (x.Index + 1))
    .Sum();

Console.WriteLine(part1);

Hand parseHand(string hand)
{
    var parts = hand.Split(" ");
    return new Hand
    {
        Cards = parts[0].Select(c => new Card
        {
            Character = c
        }).ToList(),
        Bid = Int32.Parse(parts[1])
    };
}

class Hand
{
    public List<Card> Cards { get; set; } = new();

    public int Score => int.Parse(string.Join("",Cards
        .Select(x => x.Value)
        .Select(x => x.ToString("D2")).ToList()));

    public int Bid { get; set; }
    public bool FiveOfAKind => Cards.GroupBy(x => x.Character).Count() == 1;
    
    public bool FourOfAKind => Cards.GroupBy(x => x.Character)
        .OrderByDescending(x => x.Count())
        .First().Count() == 4;

    public bool FullHouse
    {
        get
        {
            var groups = Cards
                .GroupBy(x => x.Character)
                .OrderByDescending(x => x.Count()).ToList();

            return groups.Count == 2 && groups.First().Count() == 3;
        }
    }

    public bool ThreeOfAKind
    {
        get
        {
            var groups = Cards
                .GroupBy(x => x.Character)
                .OrderByDescending(x => x.Count()).ToList();
            return groups.Count == 3 && groups.First().Count() == 3;
        }
    }

    public bool TwoPair
    {
        get
        {
            var groups = Cards
                .GroupBy(x => x.Character)
                .OrderByDescending(x => x.Count()).ToList();
            
            return groups.Count == 3 && groups[0].Count() == 2 && groups[1].Count() == 2;
        }
    }
    
    public bool OnePair
    {
        get
        {
            var groups = Cards
                .GroupBy(x => x.Character)
                .OrderByDescending(x => x.Count()).ToList();
            
            return groups.Count == 4 && groups[0].Count() == 2;
        }
    }

    public bool HighCard => Cards.GroupBy(x => x.Character).Count() == 5;
}

class Card
{
    public char Character { get; set; }

    public int Value => Character switch
    {
        >= '2' and <= '9' => int.Parse(Character.ToString()),
        'T' => 10,
        'J' => 11,
        'Q' => 12,
        'K' => 13,
        'A' => 14,
        _ => throw new Exception("Invalid card")
    };
}
class CardComparer : IComparer<List<int>>
{
    public int Compare(List<int> x, List<int> y)
    {
        for (int i = 0; i < x.Count; i++)
        {
            if (x[i] != y[i]) return y[i].CompareTo(x[i]);
        }

        return y.Count.CompareTo(x.Count);
    }
}
