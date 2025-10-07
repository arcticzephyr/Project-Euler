import Debug.Trace

maxPrimeDiv:: Int -> Int
maxPrimeDiv n = go n 2
    where
        go n k
            | n == 1 = k
            | mod n k == 0 = go (n `div` k) k 
            | (otherwise) = go n (k + 1)

main = print $ maxPrimeDiv 600851475143