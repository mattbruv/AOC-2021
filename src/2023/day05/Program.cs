var lines = File.ReadAllText("../../../input.txt").Split("\n\n");


var seeds = lines.First().Split(":")[1].Trim().Split().Select(x => Int64.Parse(x)).ToList();

var maps = lines.Skip(1)
    .Select(x => new Mapping(x))
    .ToList();

Console.WriteLine(seeds);

record Mapping(string map)
{
    private string[] Lines => map.Split("\n");

    public string From => Lines.First().Split("-")[0];
    public string To => Lines.First().Split("-")[2].Split().First();
}