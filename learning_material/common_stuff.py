# chr ord
chr(97) # outputs 'a'
ord('a') #outputs 97

# cutting string
# s[start:end:step]
s='abcdef'
# reverse
rev = s[::-1]
# get three first chars
# it always includes start index 0 and 3 - 1
s[0:3] # outputs 'abc'
s[0:0] # outputs empty ''
s[10:15]# empty


# leading zeros are not showing
bin(7) #converts number into binary string
# '0b111' - no leading zeros here
bin(12)
# '0b1100'
# this binary string needs to be read from right to the left
# 2**3, 3**2, 0, 0

# shift operations >> and <<
# x >> y - Returns x with the bits shifted to the right by y places. This is the same as dividing x//2**y
# x << y  - Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros).
# This is the same as multiplying x by 2**y
#

# let's suppose we want to shift the bits to the right by 1
bin(1029)
# '0b10000000101'
1029 >> 1 # the result is 514
# this is because the binary string 10000000101

# conversion from binary to decimal
# int(b, 2)

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

#

# to skip current element when traversing we do
a = [1,2,3]
for i in range(len(a)):
    res = a[:i] + a[i + 1]
# this
for i in range(len(a))[::-1]:
    pass
# is same as
for i in range(len(a)-1, -1, -1):
    pass

# Permutations
#### n permutations from n objects ####
#"A permutation is a (possible) rearrangement of objects." (Levin, 2016)
# To get count of possible permutations we use multiplicative principle
# Example [a,b,c]. a has 3 choices, b has 2 choices and c has 1 choice
# count = 3 * 2 * 1 = 6
# permutation of n distinct elements is n!
#### k permutations from n objects ####
# the number of k permutations of n elements is
# P(n,k) = n!/(n-k)!
#### combinations of k unique elements from n objects ####
# C(n,k) = n!/(n-k)!k! - this is also binomial coefficient

# suppose we have 2 dimensional array
B = [[7, 2, 3],[4, 5, 6],[0, 0, 1]]
# gets array of rows :
zip(B)
# gets array of cols
zip(*B)




