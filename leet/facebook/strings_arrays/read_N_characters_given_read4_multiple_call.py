#158 https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

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
    def __init__(self):
        self.i = 0
        self.j = 0
        self.tmp = [' '] * 5

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        if n <= 0:
            return 0
        self.j = 0
        if self.need_to_stop(buf, n):
            return self.j
        self.tmp = [' '] * 5
        while n > 0 and read4(self.tmp) > 0:
            self.i = 0
            if self.need_to_stop(self, buf, n):
                return self.j
            self.tmp = [' '] * 5
        return self.j


    def need_to_stop(self, buf, n):
        while self.tmp[self.i] != ' ':
            buf[self.j] = self.tmp[self.i]
            self.i += 1
            self.j += 1
            if self.j >= n:
                return True
        return False

from collections import *
import  itertools
class Solution(object):

    def __init__(self):
        self.chars = itertools.chain.from_iterable(iter(lambda buf=[0]*4: buf[:read4(buf)], []))
        print(self.chars)

    def read(self, buf, n):
        return len([buf.__setitem__(*x) for x in zip(range(n), self.chars)])


