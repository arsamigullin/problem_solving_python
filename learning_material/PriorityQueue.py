class Node:
    def __init__(self,x,y,dist):
        self.x = x
        self.y = y
        self.dist = dist

    def __lt__(self, other):
        return self.dist<other.dist


import heapq
heap = []
heapq.heappush(heap, Node(1,2,5))
heapq.heappush(heap, Node(2,4,3))

if __name__ == '__main__':
    print(heapq.heappop(heap).dist)
    print('done')