class MySolution:
    def plusOne(self, digits: list) -> list:

        i = len(digits) - 1
        rem = 1
        while i >= 0:
            total = digits[i] + rem
            if total >= 10:
                digits[i] = total - 10
            else:
                digits[i] = total
                return digits
            i -= 1

        digits.insert(0, rem)
        return digits


# another good solution
def plusOne(digits):
    num = 0
    for i in range(len(digits)):
    	num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]