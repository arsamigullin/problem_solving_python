# 1268. Search Suggestions System
# https://leetcode.com/problems/search-suggestions-system/
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        def binarySearch(tofind):
            begin = 0
            end = len(products) - 1
            result = -1
            while begin<=end:
                mid = begin+(end-begin)//2
                if products[mid].startswith(tofind) or tofind < products[mid][:len(tofind)]:
                    result = mid
                    end = mid - 1
                else:
                    begin = mid + 1
            return result
        res = []
        for i in range(len(searchWord)):
            tofind = searchWord[:i+1]
            ind = binarySearch(tofind)
            res.append([word for word in products[ind: ind + 3] if tofind==word[:len(tofind)]])
        return res