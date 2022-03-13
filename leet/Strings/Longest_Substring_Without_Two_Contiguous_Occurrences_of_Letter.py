# microsoft

def longestValidString(str) -> str:
    stack = []
    max_str = ''
    max_len = 0

    for i, ch in enumerate(str):
        if len(stack) >= 2 and stack[-1] == stack[-2] and stack[-2] == ch:
            stack = [stack[-1]]
        stack.append(ch)
        if len(stack) > max_len:
            max_str = ''.join(stack)
            max_len = len(max_str)

    return max_str

from itertools import groupby
def longestValidString2(str) -> str:
      loc, ans = '', ''
      for c, g in groupby(str):
          glen = len(list(g))
          ans = max([ans, loc + c * min(glen, 2)], key=len)
          if glen > 2:
              loc = c*2
          else:
              loc += c*glen
      return ans

if __name__ == '__main__':
    longestValidString2("aabbbaabbaabbaabb")
    longestValidString("aabbaaaaabb")
    longestValidString("aabbaabbaabbaaa")
    longestValidString("aabbababbaabaababbababaababbabababababaaababababbabaaabbbaabbabbababababaabba")