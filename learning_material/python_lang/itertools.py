import itertools

# -------------- infinite iterators ----------------
def count():
    for c in itertools.count(10):
        print(c) # 10 11 12 13 14 ...

def repeat():
    r = itertools.repeat(10,3)
    print(list(r)) # [10, 10, 10]
    for item in r:
        print(item)

def accumulate():
    import operator
    itertools.accumulate([1, 2, 3, 4, 5]) # 1 3 6 10 15
    itertools.accumulate([1, 2, 3, 4, 5], initial=100) # 100 101 103 106 110 115
    itertools.accumulate([1, 2, 3, 4, 5], operator.mul) #1 2 6 24 120

# Iterators terminating on the shortest input sequence
def gb():
    it = itertools.groupby("aaabaaabbaaa")
    for key, vals in it:
        print(key, list(vals))

if __name__ == '__main__':
    gb()
    #repeat()
    #count()