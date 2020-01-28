import typing
List = typing.List
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        nearest_root = None
        for i in range(0, len(preorder)):
            while stack and preorder[i] > stack[-1]:
                nearest_root = stack.pop()
            if nearest_root is not None and nearest_root > preorder[i]:
                return False
            stack.append(preorder[i])

        return True

if __name__ == "__main__":
    s = Solution()
    s.verifyPreorder([4,2,1,3,6,5,7])