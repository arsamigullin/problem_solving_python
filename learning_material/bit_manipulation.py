
if __name__ == "__main__":
    for i in range(1, 32):
        pass
        #print(f"{i}&1 = {i & 1}")
# num&1 = 1 for odd num
# num&1 = 0 for even num

for i in range(1, 32):
    print(f"{i}>>1 = {i >> 1}")

# checks if the num is a power of 4?
# the first option
# return num > 0 and num & (num - 1) == 0 and num % 3 == 1
# the second option
# return num > 0 and log2(num) % 2 == 0

# Check if the number is a power of 2?
x = 4
x & x - 1 == 0

# 0 - 0
# 01 - 1
# 10 - 2
# 11 - 3
# 100 - 4
# 101 - 5
# 110 - 6
# 111 - 7
# 1000 - 8
# 1001 - 9
# 1010 - 10
# 1011 - 11
# 1100 - 12
# 1101 - 13
# 1110 - 14
# 1111 - 15

# XOR with the same number is 0
x = 5
res = x^x # res is 0

# ~ just does inverting of each bits (one's complement)
# which is the same as ~x = -(x+1)
# complement of x
# Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1
x = 5
res = ~x = -6
#---------- Two's complement is about representation negative numbers--------
# According to Nisan & Schocken, the two's complement number can be gotten base on this formula (2005):
# 2**n-1 (where n is total bit)
# As a rule, when the 2’s complement method is applied to n-bit numbers, x+(-x) always sums to 2**n - a property that gives the method its name.
# for example, if we have 4 bits system then
# for number 2 the number -3 is two's complement number
# (2**4) - 2 = 16 - 2 = 14
# which is in binary representation is 1110
# according to the table below 1101 also corresponds to -2

# positive   negative
# 0 0000
# 1 0001      1111 -1
# 2 0010      1110 -2
# 3 0011      1101 -3
# 4 0100      1100 -4
# 5 0101      1011 -5
# 6 0110      1010 -6
# 7 0111      1001 -7
# 8 1000      1000 -8


# xor
#A connective in logic known as the "exclusive or," or exclusive disjunction. It yields true if exactly one (but not both) of two conditions is true
# 1 0 |1
# 0 1 |1
# 0 0 |0
# 1 1 |0

#Two's Complement binary for Positive Integers:

#0 is written as "0"
#1 is written as "1"
#2 is written as "10"
#3 is "11"
#4 is "100"
#5 is "101"
#.
#.
#1029 is "10000000101" == 2**10 + 2**2 + 2**0 == 1024 + 4 + 1

# Some TRICKS
# If one builds an array bitmask with the help of XOR operator, following bitmask ^= x strategy,
# the bitmask would keep only the bits which appear odd number of times.
# x & (-x) is a way to isolate the rightmost 1-bit, i.e. to keep the rightmost 1-bit and to set all the others bits to zero.
# Please refer to the article https://leetcode.com/articles/power-of-two/

# In	two's	complement	representation	of	signed	numbers,	positive	numbers	are
# represented	in	the	normal	way,	but	negative	numbers	are	represented	by	applying
# a	bitwise	NOT	(see	Chapter	4)	to	the	positive	version	of	a	number	(thus
# generating	the	complement),	and	then	adding	1	to	that	complement.


#  n & (-n) is a way to keep the rightmost 1-bit and to set all the other bits to 0.
# 7 & (-7) = 7 & (invert all bits of 7 + 1)= 0000111 & (1111000 + 1) = 0000111 & 1111001 = 0000001
# 7 !=1
# 16 & (-16) = 16 & (invert all bits of 16 + 1) = 00010000 & (11101111 + 1) = 00010000 & 11110000 = 00010000
# 16 == 16


#  x & (x - 1) is a way to set the rightmost 1-bit to zero.
# To subtract 1 means to change the rightmost 1-bit to 0 and to set all the lower bits to 1.
# if x & (x - 1) == 0 the number is power of two
# 4 & (4-1) = 00100 & (00100 - 1) = 00100 & 00011 = 0
# 4 is power of 2

# flipping the bit can be done by the approaches presented in 476_Number_Complement

# this is how we count bits on each number
#338. Counting Bits
class Solution:
    def countBits(self, num: int) -> list:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            if i%2 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2] + 1
        return dp


# 190. Reverse Bits