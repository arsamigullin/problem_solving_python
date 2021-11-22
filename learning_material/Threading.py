import concurrent.futures as f
import math
import random

'''
Both ProcessPoolExecutor and ThreadPoolExecutor implement the same interface concurrent.futures.Executor
the interface consists of the methods
submit(fn,*args,**kwargs)
map(fn, *iterables, timeout, chunksize=1) 
With ThreadPoolExecutor, chunksize has no effect.
shutdown(wait=True, *, cancel_futures=False)
'''

def is_prime(n):
    if n<2:
        return False
    if n == 2:
        return True
    if n%2==0:
        return False

    lim = math.floor(math.sqrt(n)) + 1
    for i in range(3, lim, 2):
        if n%i == 0:
            return False
    return True

primes = []
for p in range(100):
    primes.append(random.randint(0, 100))

import timeit

start = timeit.timeit()
map(is_prime, primes)
end = timeit.timeit()
print(f'Plain {end-start}')


with f.ThreadPoolExecutor(max_workers=10) as executor:
    start = timeit.timeit()
    fut = executor.map(is_prime, primes)
    end = timeit.timeit()
    print(f'ThreadPoolExecutor {end-start}')

with f.ProcessPoolExecutor(max_workers=3) as executor:
    start = timeit.timeit()
    fut = executor.map(is_prime, primes)
    end = timeit.timeit()
    print(f'ProcessPoolExecutor {end - start}')


if __name__ == '__main__':
    print('go')