class Solution:
    def lengthLongestPath(self, input):
        '''

        '''
        maxlen = 0
        pathlen = {0: 0}
        print(input.splitlines())
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                # for every file the length per depth in pathlen dict will be overwritten
                # with the length of the preceding this file folder
                # +1 here to cover /
                # "dir/subdir2/subsubdir2/file2.ext"
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen

if __name__ == '__main__':
    s =Solution()
    s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
    s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")