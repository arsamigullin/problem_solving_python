class Solution:
    def intToRoman(self, num: int) -> str:
        d = [(1, 'I'), (5, 'V'), (4, 'IV'), (10, 'X'), (9, 'IX'), (50, 'L'), (40, 'XL'), (100, 'C'), (90, 'XC'),
             (500, 'D'), (400, 'CD'), (1000, 'M'), (900, 'CM')]
        d.sort(reverse=True)

        res = []
        # we start from the bigger number
        for val, symbol in d:
            if num == 0:
                break
            # reps is how many times the symbol will be repeated
            # result is the next value for num
            reps, result = divmod(num, val)
            res.append(symbol * reps)
            num = result
        return ''.join(res)