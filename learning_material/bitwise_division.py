if __name__ == "__main__":

    divisor = 3
    dividend = 10
    quotient = 0
    remaining_dividend = dividend
    while remaining_dividend >= divisor:
        how_many_shifts = 0
        while divisor << (how_many_shifts + 1) <= remaining_dividend:
            how_many_shifts = how_many_shifts + 1
        remaining_dividend = remaining_dividend - (divisor<<how_many_shifts)
        quotient |= 1 <<how_many_shifts

    reminder = remaining_dividend


