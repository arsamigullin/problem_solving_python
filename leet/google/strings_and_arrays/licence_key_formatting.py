#https://leetcode.com/problems/license-key-formatting/
# since first group could contain number of char less than K we start from end
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        plain_plate = S.replace('-', '')
        rem = len(plain_plate) % K
        if rem == 0:
            res = []
        else:
            res = [plain_plate[0:rem]]
        i = rem
        while i < len(plain_plate) - K + 1:
            res.append(plain_plate[i:i + K])
            i += K
        return '-'.join(res).upper()
