class Solution:
    def countAndSay(self, n):
        next_saying = ""
        for i in range(n):
            if i == 0:
                next_saying = "1"
                continue
            if len(next_saying) == 1:
                next_saying = get_saying(next_saying)
                continue
            part = ""
            l = list()
            prev = ""
            for j in range(len(next_saying)):
                if next_saying[j] != prev:
                    prev = next_saying[j]
                    if part != "":
                        l.append(part)
                    part=next_saying[j]
                else:
                    part+=next_saying[j]
            l.append(part)
            next_saying = ''.join([get_saying(item) for item in l])
        return next_saying


def get_saying(s):
    len_s = len(s)
    if len_s > 1:
        return str(len_s) + s[0]
    else:
        return '1' + s


if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(10))