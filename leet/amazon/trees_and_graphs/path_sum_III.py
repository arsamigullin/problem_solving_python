# Definition for a binary tree node.
# the same technique is applied here subarray_sum_equals_k.py
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.ans = 0
        if not root: return 0
        cnt = collections.defaultdict(int)
        cnt[0]=1
        def preorder(r, cs, cnt):
            if not r: return
            
            cs += r.val
            if cs-sum in cnt:
                self.ans += cnt[cs-sum]
            cnt[cs]+=1
            
            preorder(r.left, cs, cnt)
            preorder(r.right, cs, cnt)
            # restore the crime scene
            cnt[cs] -= 1
            return
        preorder(root, 0, cnt)
        return self.ans




class MySolution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        cnt = 0
        d = collections.defaultdict(int)
        def find(node, lvl, parents):
            nonlocal cnt
            if node is None:
                return
            key = f"{node.val}|{lvl}"    
            if key not in d:
                d[key] = sum
            parents.append(key)
            for p in parents:
                d[p]-=node.val
                if d[p]==0:
                    cnt+=1
            find(node.left, lvl+1, parents)
            find(node.right, lvl+1, parents)
            for p in parents:
                d[p]+=node.val
            parents.pop()
        find(root, 0, [])
        return cnt

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.left = TreeNode(1)
    s = Solution()
    s.pathSum(root,8)