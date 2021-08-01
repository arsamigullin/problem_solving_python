import collections
from collections import defaultdict
from string import ascii_lowercase
from typing import List

# Time: O(N * 26 * W^2 + A), where N <= 1000 is number of words in wordList, W <= 5 is length of each words, A is total number of sequences.
# BFS costs O(E + V), where E is number of edges, V is number of vertices.
# Because words need to be existed in the wordList, so there is total N words, it's also the number of vertices.
# To find neighbors for a word, it costs O(26 * W * W), in the worst case, we have to find the neighbors of N words, so there is total O(N * 26 * W^2) edges.
# Space: O(N*W + A)
class Solution:  # 44 ms, faster than 86.16%
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)  # to check if a word is existed in the wordSet, in O(1)
        wordSet.discard(beginWord)

        def neighbors(word):
            for i in range(len(word)):  # change every possible single letters and check if it's in wordSet
                for c in ascii_lowercase:
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordSet:
                        yield newWord

        layer = {}
        layer[beginWord] = [[beginWord]]  # layer[word] is all possible sequence paths which start from beginWord and end at `word`.
        while layer:
            nextLayer = defaultdict(list)
            for word, paths in layer.items():
                if word == endWord:
                    return paths  # return all shortest sequence paths
                for nei in neighbors(word):
                    for path in paths:
                        nextLayer[nei].append(path + [nei])  # form new paths with `nei` word at the end
            wordSet -= set(nextLayer.keys())  # remove visited words to prevent loops
            layer = nextLayer  # move to new layer

        return []



if __name__ == '__main__':
    s = Solution()
    s.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if endWord not in wordList:
            return []

        size = len(beginWord)

        lookup = defaultdict(list)

        for word in wordList:
            for i in range(size):
                lookup[word[:i] + "*" + word[i + 1:]].append(word)

        cur_len = 9999

        ans = []

        "enter the first element in the queue"

        queue = collections.deque([[beginWord, 1, [beginWord]]])

        visited = {beginWord: True}

        while (queue):

            currWord, pathLength, words_till_now = queue.popleft()

            """
            instead of marking an elemnt vistied , when we insert it in the queue,
            we mark it as visited only when we pop and element
            this way , same word can be used by other curWords
            <ex :>
            "red"
            "tax"
            ["ted","tex","red","tax","tad","den","rex","pee"]                        
            and we make sure that element can not be used again           
            """
            visited[currWord] = True

            """
            run a for loop for all values for all the possible patterns for the popped word
            """

            for i in range(size):

                possibleWordPattern = currWord[:i] + "*" + currWord[i + 1:]

                for word in lookup[possibleWordPattern]:

                    if (currWord == word):
                        continue

                    """
                    if the word for the possibleWordPattern key matches with the end word we add it to the 
                    ans list
                    """

                    if (word == endWord):

                        if cur_len == pathLength + 1:

                            ans.append(words_till_now + [word])
                        elif cur_len > pathLength + 1:

                            ans = [words_till_now + [word]]

                            cur_len = pathLength + 1

                    if (word not in visited):
                        queue.append([word, pathLength + 1, words_till_now + [word]])

        return ans

