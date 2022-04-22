from queue import PriorityQueue

def play():
    p = PriorityQueue()
    p.put(4)
    p.put(1)
    p.put(6)
    while p:
        print(p.get())


if __name__ == '__main__':
    play()