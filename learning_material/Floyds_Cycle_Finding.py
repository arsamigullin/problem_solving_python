
n = 0
def f(i):
    return i+1 if i+1<n else 0


def floydCycleFinding(nums):
    # 1st part: finding k*mu, hare's speed is 2x tortoise's
    tortoise = f(0)  # f(x0) is the node next to x0
    hare = f(f(0))
    while nums[tortoise] != nums[hare]:
        tortoise = f(tortoise)
        hare = f(f(hare))

    # 2nd part: finding mu (starting point), hare and tortoise move at the same speed
    # perhaps this is redundant step since we already have a starting point which is hare
    # but if there are multiple cycles, then we want to run this step
    mu = 0
    hare = tortoise
    tortoise = 0
    while nums[tortoise] != nums[hare]:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1

    # 3rd part: finding lambda (length of cycle), hare moves, tortoise stays
    # it is important to start from here from the next point
    # otherwise it will never enter the loop
    lambd = 1
    hare = f(tortoise)
    while nums[tortoise] != nums[hare]:
        hare = f(hare)
        lambd += 1

    return lambd




if __name__ == '__main__':
    nums = [7,33,69,45,61,77,13,29,45,61,77,13,29,45]
    nums = [7, 33, 69, 45, 61, 77, 13, 29, 45, 61,77]
    n = len(nums)
    floydCycleFinding(nums)
