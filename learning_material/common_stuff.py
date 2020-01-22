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

# let's suppose we want to shift the bits to the right by 1
bin(1029)
# '0b10000000101'
1029 >> 1 # the result is 514
# this is because the binary string 10000000101

# conversion from binary to decimal
# int(b, 2)

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

# suppose we have 2 dimensional array
B = [[7, 2, 3],[4, 5, 6],[0, 0, 1]]
# to get row and an array at this row we do
# note : this we return tuple (index, ([array],)
enumerate(zip(B))
# to get col and an array at this col we do
enumerate(zip(*B))
