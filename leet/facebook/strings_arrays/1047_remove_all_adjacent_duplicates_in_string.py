# duplicate removal
# similar is 1209

class Solution:
    def removeDuplicates(self, S: str) -> str:

        stack = [['#', 0]]
        for ch in S:
            if stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == 2:
                    stack.pop()
            else:
                stack.append([ch, 1])

        return ''.join([ch * count for i, (ch, count) in enumerate(stack[1:])])


from re import sub

# beautiful recursive solution
class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = sub(r'([a-z])\1', '', S)

        return s if s == S else self.removeDuplicates(s)