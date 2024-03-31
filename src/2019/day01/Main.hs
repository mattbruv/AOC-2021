module Main where

main :: IO ()
main = do
  file <- readFile "input.txt"
  let input = lines file
  let ns = map (\x -> read x :: Integer) input
  let p1 = sum $ map calc ns
  let p2 = sum $ map (sum . reduce []) ns
  print p1
  print p2

calc :: Integer -> Integer
calc x = div x 3 - 2

reduce :: [Integer] -> Integer -> [Integer]
reduce ns n =
  let fuel = calc n
   in case fuel of
        _ | fuel <= 0 -> ns
        _ -> reduce ns fuel ++ [fuel]
