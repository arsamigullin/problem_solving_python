import collections
import threading


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.queue = collections.deque()
        self.max_size = capacity
        # we on purpose initialized Semaphore with the counter > 0
        # That will ensure the queue will not exceed the capacity
        self.semaphor_enq = threading.Semaphore(capacity)
        # this is initialized with 0 because
        # in case of calling deque first it will block the current thread because counter is set to 0
        self.semaphore_deq = threading.Semaphore(0)


    #
    def enqueue(self, element: int) -> None:
        print(f"{threading.current_thread().getName()} enqueue is blocked")
        self.semaphor_enq.acquire()
        self.queue.append(element)
        print(f"added element {threading.current_thread().getName()} enqueue is released")
        self.semaphore_deq.release()

    # if
    def dequeue(self) -> int:
        self.semaphore_deq.acquire(blocking=True)
        print(f"{threading.current_thread().getName()} dequeue is blocked")
        el = self.queue.popleft()
        print(f"{threading.current_thread().getName()} dequeue is released")
        self.semaphor_enq.release()
        return el

    def size(self) -> int:
        return len(self.queue)


from collections import deque
import threading


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.que = deque()
        self.cv = threading.Condition()
        self.cap = capacity

    def enqueue(self, element: int) -> None:
        self.cv.acquire()
        while len(self.que) >= self.cap:
            self.cv.wait()
        self.que.append(element)
        self.cv.notify()
        self.cv.release()

    def dequeue(self) -> int:
        self.cv.acquire()
        while len(self.que) == 0:
            self.cv.wait()
        r = self.que.popleft()
        self.cv.notify()
        self.cv.release()


# Important to create a thread we use Start and NOT Run
if __name__ == '__main__':
    b = BoundedBlockingQueue(3)
    for i in range(3):
        if i == 0:
            t = threading.Thread(target=b.enqueue,args=[5])
            t.start()
            #print(t.getName() + " " + str(t.ident))
            t = threading.Thread(target=b.dequeue)
            t.start()
            #print(t.getName() + " " + str(t.ident))
        elif i == 1:
            t = threading.Thread(target=b.enqueue,args=[3])
            t.start()
            #print(t.getName() + " " + str(t.ident))
            t = threading.Thread(target=b.enqueue, args=[6])
            t.start()
            #print(t.getName() + " " + str(t.ident))
        elif i == 2:
            t = threading.Thread(target=b.dequeue)
            t.start()
            #print(t.getName() + " " + str(t.ident))
            t = threading.Thread(target=b.dequeue)
            t.start()
            #print(t.getName() + " " + str(t.ident))

