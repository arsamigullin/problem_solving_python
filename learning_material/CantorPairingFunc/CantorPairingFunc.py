'''
Cantor pairing func is only for 0 and positive coordinates
'''
def cantor_pairing_func(x, y):
    x = map_number(x)
    y = map_number(y)
    return 0.5 * (x + y) * (x + y + 1) + y

# this is to map negative number to positive
def map_number(x):
    return 2 * x if x >= 0 else -2 * x - 1