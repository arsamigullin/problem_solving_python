#157 https://leetcode.com/problems/read-n-characters-given-read4/
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        tmp = [' '] * 5
        j = 0
        while read4(tmp) > 0:
            i = 0
            while tmp[i] != ' ':
                buf[j] = tmp[i]
                if j >= n:
                    break
                i += 1
                j += 1
            tmp = [' '] * 5

        return j


class Solution2:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        idx = 0
        buf4 = [' ']*4
        while n:
            n4 = read4(buf4)
            if n4==0: break
            nkeep = min(n, n4)
            buf[idx:idx+nkeep]=buf4[:nkeep]
            idx += nkeep
            n -= nkeep
        return idx