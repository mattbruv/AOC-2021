var lines = File.ReadAllText("../../../input.txt").Split("\n\n");

var seeds = lines.First().Split(":")[1].Trim().Split().Select(x => Int64.Parse(x)).ToList();

var maps = lines.Skip(1)
    .Select(x => new Mapping(x))
    .ToList();

maps.First().Apply()

Console.WriteLine(test);

record Mapping(string map)
{
    private string[] Lines => map.Split("\n");

    public string From => Lines.First().Split("-")[0];
    public string To => Lines.First().Split("-")[2].Split().First();
    public List<Map> Mappings => Lines.Skip(1).Select(x => new Map(x)).ToList();

    public long Apply(long source) => Mappings.Aggregate(source, (acc, x) => x.ToDestination(acc));
}

record Map(string line)
{
    private long DestinationRangeStart => long.Parse(line.Split()[0]);
    private long SourceRangeStart => long.Parse(line.Split()[1]);
    private long RangeLength => long.Parse(line.Split()[2]);

    public long ToDestination(long source)
    {
        if (source >= SourceRangeStart && source <= SourceRangeStart + RangeLength)
            return DestinationRangeStart + source % SourceRangeStart;

        return source;
    }
}