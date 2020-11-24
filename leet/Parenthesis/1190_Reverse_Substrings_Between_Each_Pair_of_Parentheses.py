import collections


class Solution:
    def reverseParentheses(self, s):
            stack = collections.defaultdict(list)
            level = 0
            for i in range(len(s)):
                if s[i]=='(':
                    level +=1
                    stack[level].append(i)
                elif s[i]==')':
                    start = stack[level].pop()
                    level-=1
                    # this not to chatch index out of range exception
                    s = s[:start]+'#'+s[start+1:i][::-1]+'#'+s[i+1:]
            return s.replace('#','')

if __name__ == '__main__':
    s = Solution()
    s.reverseParentheses('(u(love)i)')