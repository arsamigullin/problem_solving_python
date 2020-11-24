import itertools


def main(n):
    items = [i for i in range(n)]
    c = [itertools.combinations(items, j) for j in range(1, n+1)]
    c = itertools.chain(*c)
    print(list(c))


def understand_chain():
    l1 = [1,2,3]
    l2 = [4,5,9]

    # will prints [1, 2, 3, 4, 5, 9]
    print(list(itertools.chain(l1, l2)))
    # will prints [1, 2, 3, 4, 5, 9]
    print(list(itertools.chain(*[l1, l2])))


if __name__ == '__main__':
    understand_chain()
    #main(3)