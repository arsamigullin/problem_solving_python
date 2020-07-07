# this is permutation k of n

# Permutations
#### n permutations from n objects ####
#"A permutation is a (possible) rearrangement of objects." (Levin, 2016)
# To get count of possible permutations we use multiplicative principle
# Example [a,b,c]. a has 3 choices, b has 2 choices and c has 1 choice
# count = 3 * 2 * 1 = 6
# permutation of n distinct elements is n!
#### k permutations from n objects ####
# the number of k permutations of n elements is
# P(n,k) = n!/(n-k)!
#### combinations of k unique elements from n objects ####
# C(n,k) = n!/(n-k)!k! - this is also binomial coefficient

def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)


def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


if __name__ == '__main__':
    from itertools import product
    for a, b, c in product(range(2), repeat=3):
        print(f"{a} {b} {c} {(not a and b and c) or (a and not b and c)}")

    print('third')
    for a, b, c in product(range(2), repeat=3):
        print(f"{a} {b} {c} {int((not a and b and c) or (a and not b and c) or (a and b and not c) or (not a and not b and not c))}")

    print('fourth')
    for a, b, c in product(range(2), repeat=3):
        nor = not((not a and b and c) or (a and not b and c) or (a and b and not c) or (not a and not b and not c))
        nand1 = not (nor and nor)
        nand2 = not (nand1 and nand1)
        nand3 = (not nand2 or not nand2)
        print(f"{a} {b} {c} {int(nand3)}")




    # for p in product(range(2), repeat=3):
    #     print(p)

    for p in product([1,2,3], repeat=3):
        print(p)


    for p in permutations("AAB"):
        print(p)
    # ('A', 'A', 'B')
    # ('A', 'B', 'A')
    # ('A', 'A', 'B')
    # ('A', 'B', 'A')
    # ('B', 'A', 'A')
    # ('B', 'A', 'A')

    for p in permutations("AAB", 2):
        print(p)

    # ('A', 'A')
    # ('A', 'B')
    # ('A', 'A')
    # ('A', 'B')
    # ('B', 'A')
    # ('B', 'A')

    for p in permutations([3,2,1]):
        print(p)

    # (3, 2, 1)
    # (3, 1, 2)
    # (2, 3, 1)
    # (2, 1, 3)
    # (1, 3, 2)
    # (1, 2, 3)


