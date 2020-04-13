import typing
List = typing.List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s or len(s) > 12:
            return []
        res = []
        segemntSize = 3 # the size 
        def is_valid(ip):
            return not ((len(ip) > 1 and ip[0] == '0') or int(ip) > 255)

        def helper(ip, leftsegments, comb):
            if ip == "":
                return
            # once no segments left
            # this means we are at latest segments,
            # so, we must add it as it is
            # since we cannot divide it
            if leftsegments == 0:
                if is_valid(ip):
                    comb.append(ip)
                    res.append('.'.join(comb))
                    comb.pop()
            else:
                for j in range(segemntSize):
                    # this checks if the rest part of numbers (len(ip) - j - 1) is greater than
                    # can be fit to the max allowed size (segemntSize * leftsegments)
                    if (len(ip) - j - 1) > segemntSize * leftsegments:
                        continue
                    ippart = ip[:j + 1]
                    if is_valid(ippart):
                        comb.append(ippart)
                        helper(ip[j + 1:], leftsegments - 1, comb)
                        comb.pop()
        # after first calling only 3 segments left XXX.YYY.YYY.YYY
        helper(s, 3, [])
        return res