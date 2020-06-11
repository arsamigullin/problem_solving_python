# monotonous stack
# leading zero removal
# similar: 670
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i, v in enumerate(num):

            while k > 0 and stack and stack[-1] > v:
                stack.pop()
                k -= 1
            if not stack:
                if v != "0":
                    stack.append(v)
            else:
                stack.append(v)
        while stack and k > 0:
            stack.pop()
            k -= 1
        return "0" if not stack else ''.join(stack)


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []

        # Construct a monotone increasing sequence of digits
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)

        # - Trunk the remaining K digits at the end
        # - in the case k==0: return the entire list
        finalStack = numStack[:-k] if k else numStack

        # trip the leading zeros
        return "".join(finalStack).lstrip('0') or "0"