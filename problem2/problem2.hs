fibonacci = 1:1: zipWith (+) fibonacci (tail fibonacci)
main = print $ sum $ filter even $ takeWhile (<4000000) fibonacci
