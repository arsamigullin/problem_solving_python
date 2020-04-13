import typing
List = typing.List

class SolutionMy:
    '''
    Divide and conquer principle
    '''
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        dist = []
        start = 0
        # here we gathering start and end positions of each word
        for i in range(len(s)):
            if s[i].strip() == '':
                dist.append((start, i))
                start = i + 1
            elif i == len(s) - 1:
                dist.append((start, i + 1))

        def helper(d):
            # once there is only one word lef just return
            # since we must do revers word by word
            if len(d) <= 1:
                return
            # otherwise we going to split the words
            if len(d) >= 2:
                mid = len(d) // 2
                fp = d[:mid] # first part of the words
                sp = d[mid:] # second part of the words
                # try more split
                helper(fp)
                helper(sp)
                # b1 beginning of the first word, e1 end of the first word
                b1, e1 = fp[0][0], fp[-1][1]
                # the same
                b2, e2 = sp[0][0], sp[-1][1]
                # consider the example
                # [s,k,y, ,b,l,u,e]
                # b1, e1 = 0, 3
                # b2, e2 = 4, 8
                # we want to paste b,l,u,e from the beginning, i.e. from b1 all the way of length of b,l,u,e (i.e. e2 - b2)
                # we want to paste s,k,y from the length of s,k,y till e2
                s[b1: b1 + (e2 - b2)], s[e2 - (e1 - b1): e2] = s[b2:e2], s[b1:e1]
                s[b1 + (e2 - b2)] = ' ' # do not forget white space

        helper(dist)


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        """

        i_start = 0
        L = len(s)

        # we reverse each word here
        # the example is [s,k,y, ,b,l,u,e]
        for i in range(L):
            if s[i] == ' ':
                self._reverse(s, i_start, i - 1)
                i_start = i + 1

        # after loop above we have
        # [y,k,s, ,b,l,u,e]
        # since the loop did not cover the latest word (blue)
        # we call one more reverse so now we have
        # [y,k,s, ,e,u,l,b]
        self._reverse(s, i_start, L - 1)
        # here we do full reverse
        self._reverse(s, 0, L - 1)
        # ther result is
        # [b,l,u,e, ,s,k,y]

    def _reverse(self, s, s_idx, e_idx):

        _s, _e = s_idx, e_idx

        while _s < _e:
            s[_s], s[_e] = s[_e], s[_s]
            _s += 1
            _e -= 1

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        # ''.join(s) produces 'the sky is blue'
        # ''.join(s).split() produces ['the', 'sky', 'is', 'blue']
        # ' '.join(''.join(s).split()[::-1]) ['blue', 'is', 'sky', 'the']
        # s[:] to assign to the same symbols
        s[:] = list(' '.join(''.join(s).split()[::-1]))

if __name__ == "__main__":
    s = Solution()
    s.reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])