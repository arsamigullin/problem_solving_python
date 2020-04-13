import collections
from typing import List


class SolutionMy:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q = collections.deque()
        while deck:
            if q:
                q.appendleft(q.pop())
                q.appendleft(deck.pop())
            else:
                q.append(deck.pop())
        return q


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        index = collections.deque([x for x in range(len(deck))])
        ans = [0] * len(deck)
        for card in deck:
            ans[index.popleft()] = card
            if index:
                # after we put the card aside, we move the current index to the end if index array
                # doing so, the numbers from deck will be put in the correct order
                index.append(index.popleft())
        return ans
