arr = [2, 4, 76]
arr = iter(arr)


def main():
    isFirst = True
    while True:
        N = next(arr, 0) # N = input()
        if N <= 0:
            break
        if not isFirst:
            print('')
        noSolution = True
        isFirst = False
        # 01234 -  the smallest five digit  number
        # 1234 * 80(the condition in the problem) is the largest number
        for fghjk in range(1234, (98765 // N) + 1):
            abcde = fghjk * N
            tmp = abcde
            # since we are allowed to have 0 at the beginning
            # having number less than 10000 means we used 0th bit
            # or in other words fghjk < 10000 means the number starts with 0, for example 01234
            # (and we must count 0th bit)
            used = fghjk < 10000

            # here we check each digit to be uniquely used by marking an appropriate bit in 'used' variable
            #
            while tmp != 0:
                # According to Khalim (page 62) to set jth bit to 1 on the number num we do num|=(1<<j)
                # so, we mark (tmp%10)th bit to be 1 (meaning that digit is used)
                used |= (1 << tmp % 10)
                # go to the next digit
                tmp //= 10

            # the same we do with fghjk
            tmp = fghjk
            while tmp != 0:
                used |= (1 << tmp % 10)
                tmp //= 10

            # if used id equal 1023 ( (1<<10)-1) that means all 10 digits in both numbers are uniquely used
            if used == (1 << 10) - 1:
                print('{:05}/{:05} = {}'.format(abcde, fghjk, N))
                noSolution = False

        if not noSolution:
            print('There are no solutions for {}.'.format(N))


if __name__ == '__main__':
    main()
