class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {'9':'6', '0':'0', '8':'8', '6':'9', '1':'1'}
        res = []
        for i, n in range(num)[::-1]:
            if n not in d:
                return False
            res.append(n)
        return ''.join(res) == num
