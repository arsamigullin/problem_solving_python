class Solution:
    def validIPAddress(self, IP: str):
        ipv4 = IP.split('.')
        if len(ipv4[0]) == len(IP):
            ipv6 = IP.split(':')
            if len(ipv6[0]) == len(IP):
                return 'Neither'
            else:
                return self.check_ipv6(ipv6)
        else:
            return self.check_ipv4(ipv4)

    def check_ipv4(self, ip):
        if len(ip) != 4:
            return 'Neither'
        else:
            for i in range(len(ip)):
                if len(ip[i]) > 3 or len(ip[i])<=0:
                    return 'Neither'
                if  ip[i].isnumeric():
                    if int(ip[i])<0 or int(ip[i])>255:
                        return 'Neither'
                else:
                    return 'Neither'
                if len(ip[i]) > 1 and ip[i][0] == '0':
                    return 'Neither'
            return 'IPv4'

    def check_ipv6(self, ip):
        allowed_chars = ['A', 'B', 'C', 'D', 'E', 'F']
        if len(ip) != 8:
            return 'Neither'
        else:
            for i in range(len(ip)):
                if len(ip[i]) > 4 or len(ip[i])<=0:
                    return 'Neither'
                for j in range(len(ip[i])):
                    sym = ip[i][j]
                    if not (65<=ord(sym.upper())<=90) and  not (48<=ord(sym.upper())<=57):
                        return 'Neither'
                    if 65<=ord(sym.upper())<=90 and sym.upper() not in allowed_chars:
                        return 'Neither'
            return 'IPv6'

    # much shorter solution
    def validIPAddress(self, IP):
        def is_hex(s):
            hex_digits = set("0123456789abcdefABCDEF")
            for char in s:
                if not (char in hex_digits):
                    return False
            return True

        ary = IP.split('.')
        if len(ary) == 4:
            for i in range(len(ary)):
                if not ary[i].isdigit() or not 0 <= int(ary[i]) < 256 or (ary[i][0] == '0' and len(ary[i]) > 1):
                    return "Neither"
            return "IPv4"
        ary = IP.split(':')
        if len(ary) == 8:
            for i in range(len(ary)):
                tmp = ary[i]
                if len(tmp) == 0 or not len(tmp) <= 4 or not is_hex(tmp):
                    return "Neither"
            return "IPv6"
        return "Neither"


if __name__ == "__main__":
    s = Solution()
    s.validIPAddress("01.01.01.01")
    s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")