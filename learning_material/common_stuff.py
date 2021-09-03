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



# suppose we have 2 dimensional array
B = [[7, 2, 3],[4, 5, 6],[0, 0, 1]]
# gets array of rows :
zip(B)
# gets array of cols
zip(*B)

# convert int to str of fixed length (size 4)
def int_to_str(num):
    sb = [chr(num >> (i * 8) & 0xff) for i in range(4)]
    sb.reverse()
    return ''.join(sb)

# this function is counterpart of the one that is right above
# i.e. it converts string into back into int
def str_to_int(val):
    res = 0
    for ch in val:
        res = res * 256 + ord(ch)
    return res

# n*(n+1)/2 - this is the formula of sum of numbers from 0 to n


#         This must be remembered
#         Given position of 1-dimensional array i, to get the position of 2-dimensional array we do the following
#         arr[i//column_count][i%column_count]

# From 2D to 1D:
# https://stackoverflow.com/questions/16790584/converting-index-of-one-dimensional-array-into-two-dimensional-array-i-e-row-a
# index = x + (y * width) from top to the bottom
# index = y + (x * height) from left to right

#generating pyramid
A = [[0] * k for k in range(1, 102)]

# finding cycle in linked list
head =  None # some head
slow = fast = head
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:
        print('cycle found')

matrix = [[1,2,3,][1,2,3]]
dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        # this is the formula for prefix sum of 2D array
        # left element + top element + prev item from orig matrix - diagonal element
        dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] + matrix[i][j] - dp[i][j]

if __name__ == '__main__':

    int_to_str(58)
    # this is how we find first two min values
    # having only one iteration
    first = second = 0
    for i in range(10):
        if first_min is None or i < first:
            second_min = first_min
            first_min = i
        elif second_min is None or i < second:
            second_min = i
    print(first,second)
