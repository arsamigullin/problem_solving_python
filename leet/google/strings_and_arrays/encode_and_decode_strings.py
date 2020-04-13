# 271. Encode and Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings/

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        # this is how we detect empty array of string
        if len(strs) == 0:
            return chr(258)

        # encode here is a workaround to fix BE CodecDriver error
        return chr(257).join(x for x in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        # this is how we understand
        if s == chr(258):
            return []
        return s.split(chr(257))


class Codec:
    def len_to_str(self, x):
        """
        Encodes length of string to bytes string
        """

        x = len(x)

        # the benefit of this approach is it gets us fixed length of x
        # so when parsing the string we could we can use it

        # the idea is we want to convert each byte to the byte string
        # to do that we will iterate over num 4 with iteration variable i
        # we can think of i as the number of byte chunk of x
        # each iteration we do:
        # 1.shift x to the i*8 bits. In other words we get the next rightmost bits.
        #   Let's denote this operation as shift This is the same as divide the number to 2**(i*8)
        #   Initially we i is 0, so no shift will be applied in the first iteration
        # 2. shift & 0xff. By doing this we take/cut the right most 8 bits. 0xff is 256 (11111111)

        # let's consider example x = 125684  bin = '00000000 00000001 11101010 11110100'
        # 1 iteration. i = 0
        # x>>0 = 125684 (no shift has been applied)
        # 125684 & 0xff = 00000000 00000001 11101010 11110100 & 11111111 = 11110100 (244) (so we got 8 rightmost bits)
        # chr(244) is 'ô'

        # 2 iteration i = 1. We will shift the bits we already handled in the first iteration
        # x >> 8 = 00000000 00000001 11101010 (490)
        # 490 & 0xff = 11101010 (234)
        # chr(234) is 'ê'

        # 3 iteration. We will shift the bits we already handled in the first iteration
        # x >> 16 = 00000000 00000001 (1)
        # 1 & 0xff = 1
        # chr(1) is '\x01'

        # 4 iteration. We will shift the bits we already handled in the first iteration
        # x>>32 = 00000000 (0)
        # 0 & 0xff = 0
        # chr(0) is '\x00'

        # bytes array is ['ô', 'ê', '\x01', '\x00']
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        # encode here is a workaround to fix BE CodecDriver error
        return ''.join(self.len_to_str(x) + x for x in strs)

    def str_to_int(self, bytes_str):
        """
        let's assume we got this ['\x00', '\x01', 'ê', 'ô']
        So, these are char we composed in len_to_str(self, x)
        NOTE: we could easily replay *256 by shifting the bits to the left on 8 bits
        1 iteration ch is '\x00'
            ord(ch) is 0
            result = result * 256 + 0
            result = 0 * 256 + 0
        2 iteration ch is '\x01'
          ord(ch) is 1
          result = 0 * 256 + 1 = 1
        3 iteration ch is 'ê'
            ord(ch) is 234
            result = 1 * 256 + 234 = 490
        4 iteration ch is 'ô'
            ord(ch) is 244
            result = 490 * 256 + 244 = 125684

        """

        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result

    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        x = '\x00\x00\x00\x00\x00\x00\x00\x00'
        b = bx
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i: i + 4])
            i += 4
            output.append(s[i: i + length])
            i += length
        return output

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))