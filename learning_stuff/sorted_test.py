class LinkNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next
l = [LinkNode(4,None),LinkNode(3,None), LinkNode(5,None)]

if __name__ == "__main__":
    res = sorted(l, key=lambda x: x.val)
    print(res)
