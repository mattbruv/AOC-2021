var input = File.ReadAllLines("input.txt");

var grid = new Grid(input);

Console.WriteLine($"{grid.Width}x{grid.Height}");

/*
var entry = grid.EntryAt(new Point(0, 12));

var grouping = grid.Groupings([entry], entry);
Console.WriteLine(grouping.Length);
*/

var groupings = grid.AllGroupings();

var totals = groupings.Select(group => new
{
    Edges = group.Select(grid.Edges).Sum(),
    Area = group.Length
});

Console.WriteLine(totals.Select(x => x.Area * x.Edges).Sum());

public record Grid(string[] Text)
{
    public int Width => Text.First().Length; 
    public int Height => Text.Length;

    private bool InBounds(Point point) => point is { X: >= 0, Y: >= 0 } && point.X < Width && point.Y < Height;

    private readonly Point[] _offsets =
    [
        new Point(-1, 0), // left
        new Point(1, 0), // right
        new Point(0, -1), // up
        new Point(0, 1) // down
    ];

    public Entry EntryAt(Point point)
    {
        return new Entry(point, Text[point.X][point.Y]);
    }

    private Entry[] Neighbors(Point point)
    {
        return _offsets
            .Select(offset => new Point(point.X + offset.X, point.Y + offset.Y))
            .Where(InBounds)
            .Select(EntryAt)
            .ToArray();
    }

    public int Edges(Entry e)
    {
        var neighbors = Neighbors(e.Location)
            .Where(n => n.Character == e.Character);

        return 4 - neighbors.Count();
    }

    public Entry[][] AllGroupings()
    {
        Entry[][] groupings = [];

        for (var x = 0; x < Width; x++)
        {
            for (var y = 0; y < Height; y++)
            {
                // Console.WriteLine($"{x}, {y}");
                var e = EntryAt(new Point(x, y));
                // check if this entry isn't already somewhere in our groupings
                if (groupings.Any(g => g.Contains(e))) continue;
                
                var grouping = Groupings([e], e);
                groupings = groupings.Append(grouping).ToArray();
            }
        }

        return groupings;
    }
    
    // initial approach I used was too slow, or had an error at (0, 12)
    // ChatGPT proposed this, and it's actually pretty fast and interesting
    // Avoids recursion by using a stack of entries, and a hashmap to track visited entries
    public Entry[] Groupings(Entry[] entriesSoFar, Entry entry)
    {
        var visited = entriesSoFar.ToHashSet(); // Keep a set of visited entries
        var stack = new Stack<Entry>();
        stack.Push(entry);

        while (stack.Count > 0)
        {
            var current = stack.Pop();
            visited.Add(current);

            var neighbors = Neighbors(current.Location)
                .Where(e => e.Character == current.Character)
                .Where(e => !visited.Contains(e)); // Only unvisited neighbors

            foreach (var neighbor in neighbors)
            {
                stack.Push(neighbor); // Add neighbors to stack for further processing
            }
        }

        return visited.ToArray(); // Convert the visited set to an array
    }

    /*
    public Entry[] Groupings(Entry[] entriesSoFar, Entry entry)
    {
        var newNeighbors = Neighbors(entry.Location)
            .Where(e => e.Character == entry.Character)
            .Where(e => !entriesSoFar.Contains(e))
            .ToArray();

        var allEntries = entriesSoFar
            .Concat(newNeighbors)
            .ToArray();
        
        return allEntries.Concat(
            newNeighbors
                .SelectMany(x => Groupings(allEntries, x))
                .Where(x => !allEntries.Contains(x))
                .ToArray()
        )
        .ToHashSet()
        .ToArray();
    }
    */
}

public record Entry(Point Location, char Character);
public record Point(int X, int Y);