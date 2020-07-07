import threading
import asyncio


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.done = False
        self.fizzbuzzsem = threading.Semaphore(0)
        self.fizzsem = threading.Semaphore(0)
        self.buzzsem = threading.Semaphore(0)
        self.numsem = threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz) -> None:
        while True:
            self.fizzsem.acquire()
            if self.done:
                break
            printFizz()
            self.numsem.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.buzzsem.acquire()
            if self.done:
                break
            printBuzz()
            self.numsem.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fizzbuzzsem.acquire()
            if self.done:
                break
            printFizzBuzz()
            self.numsem.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.numsem.acquire()
            if i % 15 == 0:
                self.fizzbuzzsem.release()
            elif i % 5 == 0:
                self.buzzsem.release()
            elif i % 3 == 0:
                self.fizzsem.release()
            else:
                printNumber(i)
                self.numsem.release()
        self.numsem.acquire()
        self.done = True
        self.fizzbuzzsem.release()
        self.buzzsem.release()
        self.fizzsem.release()


if __name__ == '__main__':
    n = 5
    s = FizzBuzz(n)
    n = n - 1
    threads = []
    for i in range(n + 1):
        if i%n == 0:
            threads.append(threading.Thread(target=s.number, args=[lambda x: print(x)]))

        if i%n == 1:
            threads.append(threading.Thread(target=s.buzz, args=[lambda: print('buzz')]))
        if i%n == 2:
            threads.append(threading.Thread(target=s.fizzbuzz, args=[lambda: print('fizzbuzz')]))
        if i%n == 3:
            t = threading.Thread(target=s.fizz, args=(lambda: print('fizz'),))
            threads.append(t)
        if i%n == 4:
            t = threading.Thread(target=s.fizz, args=(lambda: print('fizz'),))
            threads.append(t)
    for t in threads:
        t.run()
