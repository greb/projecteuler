import System.IO

solve :: [[Int]] -> Int
solve = (!! 0) . foldr1 maxLine 

maxLine :: [Int] -> [Int] -> [Int]
maxLine xs ys = zipWith max as bs
  where as = zipWith (+) xs ys
        bs = zipWith (+) xs (tail ys)

parseFile :: String -> [[Int]]
parseFile = map parseLine . lines
  where parseLine = map read . words

main = readFile "problem18.txt" >>= (print . solve . parseFile)
