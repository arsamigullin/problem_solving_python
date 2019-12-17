#https://leetcode.com/problems/multiply-strings/
def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    n, m = 0, 0
    for i in num1:
        n = n * 10 + (ord(i) - 48)
    for j in num2:
        m = m * 10 + (ord(j) - 48)
    return str(n * m)

def multiply1(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    def conv(num):
        power = len(num) - 1
        res = 0
        for n in num:
            res+=10 ** power * (ord(n)-48)
            power -=1
        return res
    return str(conv(num1) * conv(num2))

if __name__ == "__main__":
    print(multiply1("456", "123"))