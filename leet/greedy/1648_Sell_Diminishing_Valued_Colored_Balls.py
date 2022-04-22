from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        inventory.append(0)
        profit = 0
        width = 1
        for i in range(len(inventory) - 1):
            if inventory[i] > inventory[i + 1]:
                if width * (inventory[i] - inventory[i + 1]) < orders:
                    # [10, 7, 6, 5, 3]
                    # let's suppose we are at index 3 with inventory[3] equals 5
                    # self.sumRange(inventory[i + 1] + 1, inventory[i]) returns 18
                    # to count these 18 orders relatively to all inventory with i<3
                    # we must times to width
                    # think of it as cutting layer with thickness equals inventory[i] - inventory[i + 1]
                    # and lenght of layer equals width variable
                    profit += width * self.sumRange(inventory[i + 1] + 1, inventory[i])
                    orders -= width * (inventory[i] - inventory[i + 1])
                # if orders less than the layer with thickness inventory[i] - inventory[i + 1] and length width we want to cut
                # then we want to determine new thickness of the layer that would fit to the orders
                else:
                    new_layer_thickness, remaining = divmod(orders, width)
                    # note: inventory[i] is not included in sumRange function
                    profit += width * self.sumRange(inventory[i] - new_layer_thickness + 1, inventory[i])
                    # that's why we also want to add the layer with inventory[i] - new_layer_thickness and length remaining
                    profit += remaining * (inventory[i] - new_layer_thickness)
                    break
            width += 1
        return profit % (10 ** 9 + 7)

    def sumRange(self, lo, hi):
        # inclusive lo and hi
        return (hi * (hi + 1)) // 2 - (lo * (lo - 1)) // 2


if __name__ == '__main__':
    s = Solution()
    s.maxProfit([85, 11, 124, 3, 5], 27)
    s.maxProfit([2,5],4)
    s.maxProfit([7, 6, 10, 3, 5], 31)
    s.maxProfit([7, 6, 10, 3, 5], 6)
