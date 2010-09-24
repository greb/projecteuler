primes :: Integral a => [a]
primes = 2 : filter isPrime [3,5..]
  where
    intSqrt = floor.sqrt.fromIntegral
    smallerEqThen n = takeWhile (<= n)
    canidates n = smallerEqThen (intSqrt n) primes
    a `isRem` b = a `rem` b == 0
    isPrime n = not $ any (isRem n) (canidates n)

sumWhile = sumWhile' 0
  where
    sumWhile' acc p (x:xs) = if p (acc+x)
                               then sumWhile' (acc+x) p xs
                               else acc
limit = 10^6

consecutive n = sumWhile (<limit) (drop n primes)

problem50 n = if elem (consecutive n) (takeWhile (<= consecutive n) primes)
                then consecutive n
                else problem50 (n+1)

main = print (problem50 0)
