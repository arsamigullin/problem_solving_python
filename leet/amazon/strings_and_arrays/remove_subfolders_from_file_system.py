import typing
List = typing.List
# this problem
#https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        i = 0
        res = []
        cur = folder[0].split('/')
        for i in range(1, len(folder)):
            if cur == folder[i].split('/')[:len(cur)]:
                continue
            else:
                res.append('/'.join(cur))
                cur = folder[i].split('/')
        res.append('/'.join(cur))
        return res