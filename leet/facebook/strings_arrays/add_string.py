
# pretty stright forward solution
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        d = {str(i): i for i in range(11)}
        n = max(len(num1), len(num2))
        num1 = num1.zfill(n)
        num2 = num2.zfill(n)

        rem = 0
        total = ""
        for i in range(n)[::-1]:
            res = d[num1[i]] + d[num2[i]]
            rem, div = divmod(res + rem, 10)
            total = str(div) + total
        if rem > 0:
            total = str(rem) + total
        return total
