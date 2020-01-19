class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        allowed = {'0': '0', '1': '1', '8': '8', '9': '6', '6': '9'}
        converted = ''
        for i in range(len(num) - 1, -1):
            if num[i] not in allowed:
                return False
            converted = converted + allowed[num[i]]

        return converted == num
if __name__ == "__main__":
    s = Solution()
    s.isStrobogrammatic('69')