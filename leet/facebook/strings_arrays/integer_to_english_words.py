class SolutionMy:
    # first version. Very ugly code
    # the idea is to convert num into string and split the string into the group with 3 elements in each group
    # once we reached end of a group we need to tail one item from groups dictionary
    def numberToWords(self, num: int):
        if num == 0:
            return "Zero"
        res = ""
        cur_group = 1
        position = 1
        groups = {
            1: '',
            2: 'Thousand ',
            3: 'Million ',
            4: 'Billion '
        }
        single = {
            '0': '',
            '1': 'One ',
            '2': 'Two ',
            '3': 'Three ',
            '4': 'Four ',
            '5': 'Five ',
            '6': 'Six ',
            '7': 'Seven ',
            '8': 'Eight ',
            '9': 'Nine ',
        }

        decimals = {
            '0': '',
            '2': 'Twenty ',
            '3': 'Thirty ',
            '4': 'Forty ',
            '5': 'Fifty ',
            '6': 'Sixty ',
            '7': 'Seventy ',
            '8': 'Eighty ',
            '9': 'Ninety ',
        }

        tens = {
            '10': 'Ten ',
            '11': 'Eleven ',
            '12': 'Twelve ',
            '13': 'Thirteen ',
            '14': 'Fourteen ',
            '15': 'Fifteen ',
            '16': 'Sixteen ',
            '17': 'Seventeen ',
            '18': 'Eighteen ',
            '19': 'Nineteen ',
        }
        snum = str(num)

        i = len(snum) - 1
        ans = ""
        while i > -1:
            if position == 1:
                if i - 1 > -1:
                    dec = snum[i - 1] + snum[i]
                    if dec in tens:
                        i -= 2
                        position += 2
                        ans = tens[dec] + ans
                    elif dec in decimals:
                        i -= 2
                        position += 2
                        ans = decimals[dec] + ans
                    else:
                        ans = single[snum[i]] + ans
                else:
                    ans = single[snum[i]] + ans
            elif position == 2:
                ans = decimals[snum[i]] + ans

            # this 'if' separate because in the code above we can increase position and i to 2. And after increasing we need to handle position and i
            if position == 3 and i >= 0:
                tmp = '' if single[snum[i]] == '' else single[snum[i]] + 'Hundred ' # 3rd position in group will always have Hundred in it
                ans = tmp + ans

            if position == 3 or i <= 0:
                ans += '' if ans == '' else groups[cur_group]
                position = 1
                cur_group += 1
                res = ans + res
                ans = ""
            else:
                position += 1
            i -= 1
        return res.strip()

class Solution:
    def numberToWords(self, num):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                return [tens[n//10-2]] + words(n%10)
            if n < 1000:
                return [to19[n//100-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(p+1):
                    return words(n//1000**p) + [w] + words(n%1000**p)
        return ' '.join(words(num)) or 'Zero'


if __name__ == "__main__":
    s = Solution()
    print(s.numberToWords(963542369571))
