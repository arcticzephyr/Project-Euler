#We use the following brute force algorithm

#Every winning number is related to a losing number by removing one digit

#Hence for each number we will iterate through it's children to see if a losing number exists

#This algorithm works by strong induction

#It also has a time complexity of nlog(n)

#This is far too slow to check every number in [1, 10^18]

#But it is fine if we check only binary numbers in [1,2^18]

#Then every binary number, x, contributes 9*num_of_non_zeros(x)

N = 18

def num_of_non_zeros(x:int) -> int:
    sum = 0
    while (x > 0):
        x &= (x - 1)
        sum += 1
    return sum

def remove_bit(x: int, i: int) -> int:
    lower = x & ((1 << i) - 1)
    upper = (x >> (i + 1)) << i
    return upper | lower

winning_numbers = [0] * (2 ** N) # 0 indicates a losing number
num_of_winners = 0


for i in range(0,N):
    winning_numbers[2 ** i] = 1
    num_of_winners += 9

for i in range(1,2 ** N):
    if winning_numbers[i] == 1:
        continue
    iswinning = 0
    for j in range(0,i.bit_length()):
        k = remove_bit(i, j)
        iswinning = max(iswinning, 1 - winning_numbers[k])
    winning_numbers[i] = iswinning
    if winning_numbers[i] == 1:
        num_of_winners += 9 ** num_of_non_zeros(i)

print(num_of_winners)
    
    




