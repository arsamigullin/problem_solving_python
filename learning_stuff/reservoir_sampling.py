import numpy as np


def reservoir_sampling(size):
    i, sample = 0, []
    while True:
        item = yield i, sample

        i += 1
        k = np.random.randint(0, i)
        if len(sample) < size:
            sample.append(item)
        elif k < size:
            sample[k] = item