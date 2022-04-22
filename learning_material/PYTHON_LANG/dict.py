import collections

def check_default_factory():
    x = 0
    def fac():
        nonlocal x
        x+=1
        return x

    d = collections.defaultdict()
    d.default_factory = fac
    a = d[1] # 1
    a = d[8] # 2
    a = d[7] # 3
    a = d[2] # 4





if __name__ == '__main__':
    check_default_factory()