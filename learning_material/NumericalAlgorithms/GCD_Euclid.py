def euclid(a, b):
    if b == 0:
        return a
    return euclid(b, a%b)

if __name__ == '__main__':
    print(euclid(24,2880))