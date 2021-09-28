class Solution1:
    def decodeString(self, s: str) -> str:

        n = len(s)
        i = 0
        def helper():
            nonlocal i
            if i >= n:
                return ''
            j = i
            while s[i].isnumeric():
                i += 1
            times = int(s[j:i])
            cur = []
            while i < n and s[i] != ']':
                if s[i].isalpha():
                    cur.append(s[i])
                elif s[i].isnumeric():
                    cur.append(helper())
                i += 1
            return ''.join(cur) * times

        cur = []
        while i < n:
            if s[i].isalpha():
                cur.append(s[i])
            elif s[i].isnumeric():
                cur.append(helper())
            i += 1
        return ''.join(cur)

class Solution:
    def decodeString(self, s: str) -> str:

        nums = []
        i = 0

        def helper():
            nonlocal i
            if i >= len(s):
                return ''
            j = i
            while i < len(s) and s[i].isdigit():
                i += 1
            if i > j:
                nums.append(int(s[j:i]))
            curr = ""
            if i < len(s) and s[i] == '[':
                i += 1
                r = []
                while i < len(s) and s[i] != ']':
                    if s[i].isalpha():
                        r.append(s[i])
                    elif s[i].isdigit():
                        r.append(helper())
                    i += 1
                curr = nums.pop() * ''.join(r)
                if i + 1 < len(s) and s[i + 1] == ']':
                    return curr
                i += 1
            elif i < len(s) and s[i].isalpha():
                j = i
                while i < len(s) and s[i].isalpha():
                    i += 1
                curr = s[j:i]
                if i < len(s) and s[i] == ']':
                    i-=1
                    return curr
            return curr + helper()

        return helper()

if __name__ == '__main__':
    s = Solution1()
    s.decodeString("3[a]2[bc]")
    s.decodeString("3[a2[c]]")
    s.decodeString("2[a3[g]h]y")
    s.decodeString("2[a3[g]h]y")