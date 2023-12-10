
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

var part2Ordered = hands.Select(x => new {OriginalHand = x, Joker = x.JokerHand})
    .OrderBy(x => x.Joker.FiveOfAKind)
    .ThenBy(x => x.Joker.FourOfAKind)
    .ThenBy(x => x.Joker.FullHouse)
    .ThenBy(x => x.Joker.ThreeOfAKind)
    .ThenBy(x => x.Joker.TwoPair)
    .ThenBy(x => x.Joker.OnePair)
    .ThenBy(x => x.Joker.HighCard)
    .ThenBy(x => x.OriginalHand.ScorePart2)
    .ToList();

var part2 = part2Ordered
    .Select((Hand, Index) => new { Hand, Index })
    .Select(x => x.Hand.Joker.Bid * (x.Index + 1))
    .Sum();

Console.WriteLine(part2);


// not 247857527
// not 247921943 (too low)

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

    public string CardString => string.Join("", Cards.Select(x => x.Character));

    public int Score => int.Parse(string.Join("",Cards
        .Select(x => x.Value)
        .Select(x => x.ToString("D2")).ToList()));
    
    public int ScorePart2 => int.Parse(string.Join("",Cards
        .Select(x => x.ValuePart2)
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

    public Hand JokerHand
    {
        get
        {
            var chars = "23456789TQKA".Select(x => x).ToList();
            List<List<Card>> handList = new();

            foreach (var substitute in chars)
            {
                var cards = new List<Card>();

                foreach (var card in Cards)
                {
                    cards.Add(new Card()
                    {
                        Character = card.Character == 'J' ? substitute : card.Character
                    });
                }
                handList.Add(cards);
            }

            List<Hand> hands = handList.Select(x => new Hand
            {
                Cards = x,
                Bid = Bid,
            }).ToList();
            
            var ordered = hands
                .OrderByDescending(x => x.FiveOfAKind)
                .ThenByDescending(x => x.FourOfAKind)
                .ThenByDescending(x => x.FullHouse)
                .ThenByDescending(x => x.ThreeOfAKind)
                .ThenByDescending(x => x.TwoPair)
                .ThenByDescending(x => x.OnePair)
                .ThenByDescending(x => x.HighCard)
                .ThenByDescending(x => x.Score)
                .ToList();

            return ordered.First();
        }
    }
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

    public int ValuePart2 => Character switch
    {
        'J' => 1,
        _ => Value
    };
}
