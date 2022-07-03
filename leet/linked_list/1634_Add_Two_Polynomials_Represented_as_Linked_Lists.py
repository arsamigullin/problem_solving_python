# Definition for polynomial singly-linked list.
class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':

        head = res = PolyNode()

        while poly1 and poly2:
            coefEqZero = False
            if poly1.power > poly2.power:
                res.next = PolyNode(poly1.coefficient, poly1.power)
                poly1 = poly1.next

            elif poly1.power < poly2.power:
                res.next = PolyNode(poly2.coefficient, poly2.power)
                poly2 = poly2.next

            else:
                coef = poly1.coefficient + poly2.coefficient
                if coef == 0:
                    coefEqZero = True
                else:
                    res.next = PolyNode(poly1.coefficient + poly2.coefficient, poly2.power)

                poly1 = poly1.next
                poly2 = poly2.next

            if not coefEqZero:
                res = res.next
        if poly1:
            res.next = poly1
        if poly2:
            res.next = poly2

        return head.next