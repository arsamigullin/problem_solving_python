#Algo
# do not forget to initialize the stack with -1. It will allow us to get cnt if the initial bracket are valid
# for example, '()'. On '(' push onto stack. On')' we pop() from the stack unconditionally, so only -1 in stack
# now we subtracting 1(index of ')') and -1, so 1-(1) = 2
# we always push onto stack when meeting opening bracket '('
# the main idea is to pop once we've met closing bracket ')' and then get the length of valid substring by
# subtracting current position and the last index that is left in the stack
# Do not forget to initialize stack with -1
# let's consider an example '())((())'
# 0. Open br, stack is [-1, 0]
# 1. Close br, stack [-1], max is max(cnt, 1-(stack[-1]) = 2
# 2. Close br, since stack is empty, just append closing tag, so the stack is [2]
# 3. Open br, stack is [2,3]
# 4. Open br, stack is [2,3,4]
# 5. Open br, stack is [2,3,4,5]
# 6. Close br, stack is [2,3,4], max is max(cnt, 6-stack[-1])=2
# 7. close br, stack is [2,3], max is max(cnt, 7-stack[-1]) = 4

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        cnt = 0
        for i,v in enumerate(s):
            if v == ')':
                stack.pop()
                if stack:
                    cnt = max(cnt, i - stack[-1])
                else:
                    print(f"stack is empty {s}")
                    stack.append(i)
            elif v == '(':
                stack.append(i)
        return  cnt

if __name__ == "__main__":
    s = Solution()
    s.longestValidParentheses('))))')
    s.longestValidParentheses("()(()())")