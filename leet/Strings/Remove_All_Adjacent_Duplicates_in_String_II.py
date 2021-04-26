import collections


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for ch in s:
            if not stack:
                stack.append([ch, 1])
            else:
                prev_ch, prev_cnt = stack[-1]
                if prev_ch == ch:
                    if (prev_cnt + 1) % k == 0:
                        stack.pop()
                    else:
                        stack[-1][1] = prev_cnt + 1
                else:
                    stack.append([ch, 1])

            # print(stack)

        return ''.join([ch * count for ch, count in stack])


if __name__ == '__main__':
    a = Solution()
    a.removeDuplicates("pbbcggttciiippooaais",2)