class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # last occurrences
        occur = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()

        for i, c in enumerate(s):

            if c not in seen:
                # current char c is less than the latest item in stack
                # and there are also occurrences for stack[-1]
                while stack and c < stack[-1] and i < occur[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)

        return ''.join(stack)