# Algo
# we compose trie structure from the given words
# iterating over board we see if the current letter in trie (actually in top trie level)
# if it is there we start to check the current letter's neighbors
#

class Solution:
    def findWords(self, board: list, words: list) ->list:
        WORD_KEY = '$'
        # this is the longest version of the code right below
        #trie = {}
        #for word in words:
        #    node = trie
        #    for letter in word:
        #        if letter not in node:
        #            node[letter] = {}
        #        node = node[letter]
        #    node[WORD_KEY] = word
        #print(trie)

        # we compose trie from the given words
        # as a placeholder we use WORD_KEY as key and word as value
        trie = {}

        for word in words:
            node = trie
            for letter in word:
                # this adds letter with value {} if it was not in the node and returns value
                node = node.setdefault(letter,{})
            node[WORD_KEY] = word
        #print(trie)

        rowNum = len(board)
        colNum = len(board[0])
        res = []
        def backtracking(col, row, parent):
            # parent always going to be a dictionary
            curletter = board[col][row]
            curNode = parent[curletter]

            # check to see if we reached the placeholder
            # meaning we found the word
            # note we pop here
            match = curNode.pop(WORD_KEY, False)
            if match:
                res.append(match)
            #mark this element as visited
            board[row][col] = '#'
            for rowOffset, colOffset in [(0,1),(0,-1),(1,0),(-1,0)]:
                r = rowOffset + row
                c = colOffset + col
                if r >= rowNum or r < 0 or c >= colNum or c<0:
                    continue
                if not board[r][c] in curNode:
                    continue
                # not curNode is parent for its children
                backtracking(r, c, curNode)

            # unmark this back
            board[row][col] = curletter

            # this is an important optimization. This say that if curNode dictionary is empty
            # we want to remove it from parent
            # for example we have this part of trie
            # {'h':{}, curnode is empty dict
            # we remove it not to visit it again

            if not curNode:
                parent.pop(curletter)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    backtracking(i,j,trie)
        return res





if __name__ == "__main__":
    s = Solution()
    s.findWords([  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
], ["oath","pea","eat","rain"])



