
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = list(map(int, version1.split('.')))
        ver2 = list(map(int, version2.split('.')))
        if len(ver1) > len(ver2):
            ver2 = ver2 + [0] * (len(ver1) - len(ver2))
        elif len(ver1) < len(ver2):
            ver1 = ver1 + [0] * (len(ver2) - len(ver1))

        for v1, v2 in zip(ver1, ver2):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0

if __name__ == '__main__':
    s = Solution()
    s.compareVersion("1.01", "1.001.0")