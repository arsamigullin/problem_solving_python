# solution with stack
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [["#", 0]]
        for c in s:
            if c == stack[-1][0]:
                stack[-1][1] += 1
                # once we've got duplicate count
                # we extract this from stack
                # since we need to remove consecutive letters with length of k
                # the next number will contribute to the latest item of stack if the latest letter in stack the same
                # as c
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return "".join([c*i for c, i in stack])



# fastest
class Solution1:
    def removeDuplicates(self, s: str, k: int) -> str:
        while True:
            initLen = len(s)
            for ch in set(s):
                s = s.replace(ch * k, "")
            if initLen == len(s):
                return s
        return s


class Solution2:
    def removeDuplicates(self, s: str, k: int) -> str:

        def getDict(string):
            d = {}
            for ch in string[:k]:
                d[ch] = d.get(ch, 0) + 1
            return d

        let_count = getDict(s)

        i, j = 0, k
        while j < len(s):
            if len(let_count) == 1 and let_count[next(iter(let_count.keys()))] == k:
                s = s[:i] + s[j:]
                let_count = getDict(s)
                i, j = 0, k
            else:
                first = s[i]
                let_count[first] -= 1
                if let_count[first] == 0:
                    let_count.pop(first)
                second = s[j]
                let_count[second] = let_count.get(second, 0) + 1
                j += 1
                i += 1
        return s

if __name__ == '__main__':
    s = Solution()
    s.removeDuplicates("deeedbbcccbdaa", 3)
    s.removeDuplicates("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy",4)

