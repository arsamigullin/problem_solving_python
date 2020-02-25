
if __name__ == "__main__":
    for i in range(1, 32):
        pass
        #print(f"{i}&1 = {i & 1}")
# num&1 = 1 for odd num
# num&1 = 0 for even num

for i in range(1, 32):
    print(f"{i}>>1 = {i >> 1}")


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

# complement of x
# Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1
x = 5
res = ~x = -6

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


