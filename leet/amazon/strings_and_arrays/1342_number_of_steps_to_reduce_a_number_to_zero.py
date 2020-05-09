class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num <= 0: return 0
        return 1 + (self.numberOfSteps(num // 2) if num % 2 == 0 else self.numberOfSteps(num - 1))

class Solution:
    def numberOfSteps (self, num: int) -> int:
        bi = bin(num)
        # counting 1 we count how many times we will subtract
        # length of bit string is how many times will we divide
        return (len(bi[2:]) - 1) + bi.count('1')



    def numberOfSteps2(self, num: int) -> int:

        # We need to handle this as a special case, otherwise it'll return -1.
        if num == 0: return 0

        steps = 0
        power_of_two = 1

        while power_of_two <= num:
            # Apply the bit mask to check if the bit at "power_of_two" is a 1.
            if (power_of_two & num) != 0:
                steps = steps + 2
            else:
                steps = steps + 1
            power_of_two = power_of_two * 2

        # We need to subtract 1, because the last bit was over-counted.
        return steps - 1