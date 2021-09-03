# convert int to str of fixed length (size 4)
# Assuming that this works only for 32 bit integers (or alternatively 4 bytes)
# at each iteration (from 0 to 4) we chop out the the i*8 bits from the num (by shifting to the right on 0, 8, 16, 24 bits)
# for example, num = 12546537 ('0b101111110111000111101001')
# to chop out the 0th octet we do num >> 0*8 (nothing actually chopped out), the second one num>>1*8 (this chops out 8 bits),
# the third num>>2*8 (this chops out 16 bits) and so on
# then we do logical & with 8 bits. Note,zeros are cut out, so the full bit numbers are
# 0b000000101111110111000111101001 (12546537)
# 0b000000000000000000000011111111 (255)
# as we can see, the logical & will leave only bits within the range 1 and 255
# a Unicode string is a sequence of code points, which are numbers from 0 through 0x10FFFF (1,114,111 decimal).
def int_to_str(num):
    t = []
    for i in range(4):
        shift = num>>(i*8)
        shift&=0xff
        ch = chr(shift)
        t.append(ch)

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


if __name__ == '__main__':
    int_to_str(1633771873)