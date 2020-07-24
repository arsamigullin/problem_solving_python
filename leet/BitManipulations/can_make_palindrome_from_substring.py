import typing
List = typing.List

class SolutionAccum1:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        def gen():
            acc = 0
            yield acc
            for c in s:
                acc = acc^( 1<<(ord(c)-97))
                yield acc
		# xor accumulator: if ith bit is zero - there were even number of chr(i+96); if it is one - odd.
        d=[c for c in gen()]
		# accumulate result with dull popcount()
        ans=[(bin(d[l]^d[r+1]).count("1")<=2*k+1) for l,r,k in queries]

        return ans

# still not clear how it works
class SolutionAccum2:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        accu = [0] * ( len(s) + 1 )
        '''
        we create accu to store cummulative XOR
        we shift 1 to the left on associative with char number (a-0, b-1 ...) of bits 
        i.e. 1<<(ord(ch)-ord('a')) and then we do cumulative XOR to define if the count of that particular letter is even or odd

        consider this string
        s = 'abcc'
        the associative array number of this string is 0122 and initial prefix XOR array is [0,0,0,0,0], i.e. len(prefixXOR) = len(s) + 1
        each element of prefixXOR array contains the number the bit representation of which says if the count of all letters
        till the current letter is even or odd

        let's dtermine prefixXOR array
        1. s[1] = s[0] ^ (1<<0) = 0^1 = 1 (we shift 1 on 0('a') bits and then we do XOR with previous result)
           now s[1] equals 1
        2. s[2] = s[1] ^ (1<<1) = 1 ^ 2 = 3 (00000011) - the first left bit says the the count of a is odd and the second bit from left
            says that the count of b is odd as well
        3. s[3] = s[2] ^ (1<<2) = 3 ^ 4 = 7 (00000111) - the 1,2,3 bits from the left say that count of a,b,c letters is odd
        4. s[4] = s[3] ^ (1<<2) = 7 ^ 4 = 3 (00000011) - the first left bit says the the count of a is odd and the second bit from left
            says that the count of b is odd as well BUT the third bit from the left is 0, this means the count of letter c if EVEN

        so, the prefixXOR array looks like this
        [0,1,3,7,3]

        According to the problem we are to determine if we can make a palindrome from a substring (given start and end of substring) after replacing 
        at most k letters. Also, we allowed to rearrange the letters as many times as we want. That means we can deal with only the count of letters

        NOTE: Any palindrome has at most one odd count of frequency 
        for example, 'aabbbaa', {a:4 b:3}, or 'abba' {a:2 b:2}

        To determine if from substring we can make a palindrome we will do XOR betweel prefixXOR[left] and prefixXOR[right]
        i.e. prefixXOR[left] ^ prefixXOR[right]
        it will produce number the bit representation of which will contains parity count of each letter in that substring
        for example, having s = 'abcc' and prefixXor = [0,1,3,7,3] and k = 1, start = 0 and end = len(s) - 1
        prefixXor[start]^prefixXor[end] = 0 ^ 3 = 3 (011)

        To define the mininum number of letters to replace to make the substring to be a palindrome
        we devide the count of 1 to 2 (or we just shift one bit to the right which means deviding the current number to two)

        Continuing with our example, we found that for substring [0:len(s) - 1] we have two ODD frequencies (but we must have 1)
        The minimum numer
        
        '''
        for i,c in enumerate(s):
            accu[i+1] = accu[i] ^ ( 1 << (ord(c) - ord("a")))

        print(accu)


        return [ bin(accu[left] ^ accu[right+1] ).count("1") >> 1 <= k for left, right, k in queries ]

if __name__ == "__main__":
    a = [0]*27
    for i in range(26):
        a[i+1] = a[i] ^ (1 << i)
    print(a)

    s = SolutionAccum2()
    s.canMakePaliQueries("abcda", [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]])