# LCM (Least Common Multiple) of two numbers is the smallest number which can be divided by both numbers.
# For example LCM of 15 and 20 is 60 and LCM of 5 and 7 is 35.
def lcm(self, a, b):
    return (a * b) // self.gcd(a, b)


def gcd(self, a, b):
    if b == 0:
        return a
    return self.gcd(b, a % b)