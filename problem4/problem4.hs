largestPalindromeProduct:: Int
largestPalindromeProduct = maximum [x * y | x<-[1..999], y<-[1..999], elem (x*y) palindromes]
    where
        palindromes = [x*100001 + y * 010010 + z * 001100| x <- [0..9], y<-[0..9], z<-[0..9]]

main = print largestPalindromeProduct