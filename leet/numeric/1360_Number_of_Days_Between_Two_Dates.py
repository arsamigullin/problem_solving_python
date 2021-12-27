class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        #         If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
        # If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
        # If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
        # The year is a leap year (it has 366 days).
        # The year is not a leap year (it has 365 days)

        start = 1971
        year1, month1, day1 = map(int, date1.split('-'))
        year2, month2, day2 = map(int, date2.split('-'))

        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        daysInYear = sum(daysInMonth)

        def is_leap_year(year):
            return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

        def count_days(year, month, day):
            tot_days = 0
            for y in range(1971, year):
                tot_days += daysInYear
                if is_leap_year(y):
                    tot_days += 1

            for m in range(month - 1):
                tot_days += daysInMonth[m]
                if m == 1 and is_leap_year(year):
                    tot_days += 1

            tot_days += day
            return tot_days

        return abs(count_days(year2, month2, day2) - count_days(year1, month1, day1))