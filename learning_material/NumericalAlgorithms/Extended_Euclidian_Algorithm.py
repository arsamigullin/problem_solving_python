'''
According to Halim (Book2 p.292), the Euclidian algo is also able to calculate the coefficients of Bezo identity
i.e, numbers x and y such that x*a+y*b = gcd(a,b)
'''
def extEiclid(a, b):
    u, v = 0, 1
    x, y = 1, 0
    while b != 0:
        quotient = a // b
        a = b
        b = a % b
        x, u = u, x - quotient * u
        y, v = v, y - quotient * v

    return a, x, y