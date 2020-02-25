import typing
List = typing.List
# we have an array of integers. each number in this array is repeated twice, except two numbers that are repeated
# once. What are these two numbers?

# Let's say we are given an array [2,3,2,3,4,6]
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:


        bitmask = 0
        for num in nums:
            bitmask^=num
        # at this moment bit mask will store the difference between two unique numbers, i.e. 4 and 5
        # the first four numbers will be cross out because of XOR
        # 2| 00000010
        #      ^
        # 3| 00000011
        #      ^
        # 2| 00000010
        #      ^
        # 3| 00000011
        #      ^
        # 4| 00000100
        #      ^
        # 6| 00000110
        #       =
        # 2| 00000010 this is result bitmask and contains the bits that are different for 4 and 6
        # The difference here it's the bits which are different for 4 and 6.


        # this operation isolates the rightmost 1-bit, which is different between x and y.
        diff = bitmask & (-bitmask)
        # let's elaborate on -bitmask
        # according to Sunnil Tana p.143 In	two's	complement	representation	of	signed	numbers,	positive	numbers	are
        # represented	in	the	normal	way,	but	negative	numbers	are	represented	by	applying
        # a	bitwise	NOT	(see	Chapter	4)	to	the	positive	version	of	a	number	(thus
        # generating	the	complement),	and	then	adding	1	to	that	complement.

        # To get -bitmask we apply bitwise NOT to bitmask and will add 1
        #  bitmask = 00000010
        # -bitmask = 11111101 + 1 = 11111110
        # bitmask   00000010
        # &
        # -bitmask  11111110
        #  =
        # x_bitmask 00000010


        # here we do XOR over all the numbers that have 1 in position diff = bitmask & (-bitmask)
        # In our case it will be 6. The number 4 will not fall under this condition since it does not have 1
        # at that position
        x = 0
        for num in nums:
            if num & diff:
                x^=num

        # x will contain the first unique number
        # to identify the second one we do x ^ bitmask
        # x is 6        | 00000110 ^
        # bitmask is 2  | 00000010
        # y is sec num  | 00000100

        return [x, x^bitmask]




