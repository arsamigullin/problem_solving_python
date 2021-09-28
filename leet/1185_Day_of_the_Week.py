
# each leap year has 366 days instead of 365, by extending February to 29 days rather than the common 28. These extra days occur
# in each year which is an integer multiple of 4 (except for years evenly divisible by 100, but not by 400).
# The leap year of 366 days has 52 weeks and two days, hence the year following a leap year will start later by two days of the week.
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dow = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        dom = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        total_days = 0

        def hasLeapDay(year):
            return 1 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 0

        for i in range(1971, year):
            total_days += 365 + hasLeapDay(i)
        if month > 2:
            dom[1] = 29 if hasLeapDay(year) else 28
        total_days += sum(dom[:month - 1])
        total_days += day - 1
        # we add 5 here because Jan 1 1971 if Friday
        return dow[(total_days + 5) % 7]
