main = do
    input <- readFile "input.txt"
    let nums = (read <$> lines input) :: [Int]
    let part1 = calc (head nums) nums []
    let part2 = map sum $ filter (\x -> length x == 3) (group nums [])
    print $ length part1
    print $ length $ calc (head part2) part2 []

calc n [] acc = acc
calc n (x:xs) acc
    | x > n     = calc x xs (acc ++ [x])
    | otherwise = calc x xs acc

group [] acc = acc
group (x:xs) acc = group xs (acc ++ [x : (take 2 xs)])