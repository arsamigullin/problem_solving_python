# Definition for singly-linked list.

# insertion sort
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    consider the following example
    [4,3,1,2]
    '''
    def insertionSortList(self, head: ListNode) -> ListNode:
        # we create a dummy not to loose the link in case if
        # the node will be inserted at the begigning of list
        # for example, 4 > 3 and we need to move 3 to the front of 4
        # 3 is going to be inserted to the beginning of the list
        # in that case we will loose the link to the head (4)
        # having a dummy with float('-inf') we guarantee that no node will be inserted at the from of list
        # thereby the link to the dummy will never lost
        dummy = ListNode(float('-inf'))
        dummy.next = head
        node = dummy

        while node and node.next:
            # if two neighbor nodes are different
            if node.val > node.next.val:
                extracted  = node.next
                # change the next element of the left side node, since we will extract the right side node
                # to put it to the right place
                node.next = extracted.next
                nd = dummy
                prev = None
                # now we want to find the appropriate place for the extracted node
                while nd:
                    # once that place found
                    if nd.val > extracted.val:
                        # the prev node points to the extracted node
                        prev.next = extracted
                        # the extracted node points to the current node
                        extracted.next = nd
                        break
                    prev = nd
                    nd = nd.next
            else:
                node = node.next
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    l = ListNode(4)
    l.next = ListNode(3)
    l.next.next = ListNode(2)
    l.next.next.next = ListNode(1)
    l.next.next.next.next = ListNode(0)
    s.insertionSortList(l)