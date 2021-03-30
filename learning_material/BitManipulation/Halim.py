# -------------Two's complements -----------------------
# How to represent -40 ?
# there is a formula 2**N-a
# where N is the number bits we want to see (or the number of bits in a system)
# a is the number we want to represent as negative (in our case 40)
# to represent -40 we do
N = 32 # let's assume this is 32 bit system
a = 40
twocomp = 2**N - a # 4294967256
bin(twocomp) #'0b11111111111111111111111111011000'
# --------------Multiply/Divide-------------------------
S = 34
# multiply by 2
S = S << 1  # 68
# divide by 4
S = S >> 2  # 17
# divide by 2
S = S >> 1  # 8

# ------To set/turn on the jth bit------------
S = 34  #       100010
j = 3  # 1<<j = 001000
S |= (1 << j)  # 101010

# ------------Check if j-th bit is set on -------------------
S = 42  # 101010
j = 3  # 1<<j = 001000
T = S & (1 << j)  # 8
# if T is 0, the j-th bit is not set
# if T is not 0, the j-th bit is set

# -------------To clear/turn off the j-th bit----------------
S = 42  # 101010
j = 1  # ~(1<<j) = 111101
S &= ~(1 << j)

# To toggle the j-th bit
S = 40 # 101000
j=2 # #1<<j = 000100
S ^= (1 << j)
# --------------To get the value of the first from the right bit---------
S = 40
# we do and between S and -S
# S   00000000000000000000000000101000
# -S  11111111111111111111111111011000
# res 00000000000000000000000000001000
T = S & (-S) # 8

#-----------------To turn on all bits in a set of size n---------------------
# let's say the n is 3
# 1<<n = 1<<3 = 8 = 1000 (note, the len is 4 now)
n = 3
S = (1<<n)-1 # 7

#-------------------Check if the number power of 2------------
x = 4
x & (x - 1) == 0

#--------------------Check if the number power of 4 ---------------
# the first option
num = 16
res = num & (num - 1) == 0 and num % 3 == 1
# the second option
# return num > 0 and log2(num) % 2 == 0


