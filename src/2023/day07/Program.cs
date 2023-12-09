// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

var input = File.ReadAllLines("../../../input.txt");
var hands = input.Select(parseHand).ToList();

foreach (var hand in hands)
{
    Console.WriteLine(hand.Cards);
    Console.WriteLine(hand.Bid);
}

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
    public int Bid { get; set; }
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
