class Solution:
    def findStrobogrammatic(self, n):
        # 018 are only the numbers that are allowed to be in the middle
        # and middle will be presented only in case of the number is odd
        # nums will contain either '' or 0,1,8

        nums = n%2 * list('018') or ['']
        while n > 1:
            n -= 2 # since we are adding two nums simultaneously we decreasing 2
            res = []
            # on the last iteration we do not use 00, i.e [n<2:]
            for a, b in ['00','11','88','69','96'][n<2:]:
                for num in nums:
                    res.append(a + num + b)
            nums = res # we store the res to add more nums to the left and to the right side on the next iteration
        return nums

# this it sthe same but recirsive
class Solution2:
    def findStrobogrammatic(self, n):
        # 018 are only the numbers that are allowed to be in the middle
        # and middle will be presented only in case of the number is odd
        # nums will contain either '' or 0,1,8
        allowed_nums = ['00', '11', '88', '69', '96']
        nums = n % 2 * list('018') or ['']
        def find(n, res):
            n-=2
            if n<0:
                return res
            to_decorate = []
            result = []
            for a, b in allowed_nums[n<2:]:
                for num in res:
                    to_decorate.append(a+num+b)
                result += find(n, to_decorate)
                to_decorate = []
            return result
        return find(n, nums)

if __name__ == "__main__":
    s = Solution2()
    s.findStrobogrammatic(5)