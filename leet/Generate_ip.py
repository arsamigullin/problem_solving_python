from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        result = []
        n = len(s)

        def dfs(i, section, ip):
            if i >= n:
                result.append('.'.join(ip))
                return
            left_section = 4 - section
            for j in range(i, i + 4):
                part = s[i:j]

                if len(part) == 0:
                    continue
                if len(part) >= 2 and part[0] == '0':
                    break
                if len(part) >= 2 and part[0] > '2':
                    continue
                if left_section * 3 < n - j - 1:
                    # print(part)
                    continue
                ip.append(part)
                dfs(j, section + 1, ip)
                ip.pop()


        dfs(0, 1, [])
        return result

if __name__ == '__main__':
    s = Solution()
    s.restoreIpAddresses("25525511135")